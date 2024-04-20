import asyncio
import time
from typing import AsyncGenerator

from asgiref.sync import sync_to_async
from django.http import (
    HttpRequest,
    HttpResponseBase,
    HttpResponse,
    StreamingHttpResponse,
)
from django.template import loader, TemplateDoesNotExist

from pluto_rt.ops import get_rt_queue_handle

SSE_CLOSE = "event: close\ndata: \n\n"


async def rt_sse_content(
    request: HttpRequest, queue_name: str, item_template: str
) -> AsyncGenerator[str, None]:
    """Deliver event stream of formatted messages from the item template."""
    mqueue = get_rt_queue_handle(queue_name)
    queue_index = 0
    count = 100
    keepalive_interval = 10  # seconds
    last_message_time = time.time()

    while True:
        items = await sync_to_async(mqueue.range)(queue_index, queue_index + count)
        now = time.time()
        if not items:
            if now - last_message_time > keepalive_interval:
                last_message_time = now
                yield "event: keepalive\ndata: \n\n"
            await asyncio.sleep(0.1)
            continue
        last_message_time = now
        queue_index += len(items)
        for item in items:
            if item == mqueue.QUEUE_EXHAUSTED:
                yield SSE_CLOSE
                return
            try:
                lines = loader.render_to_string(item_template, {"item": item}).strip().split("\n")
                formatted_data = "\n".join(f"data: {line}" for line in lines)
                yield f"event: message\n{formatted_data}\n\n"
            except TemplateDoesNotExist:
                yield "data: template not found\n\n"
                yield SSE_CLOSE
                return


def rt_sse(request: HttpRequest, queue_name: str, item_template: str) -> HttpResponseBase:
    return StreamingHttpResponse(
        streaming_content=rt_sse_content(request, queue_name, item_template),
        content_type="text/event-stream",
    )


def rt_polling(request: HttpRequest, queue_name: str, item_template: str) -> HttpResponse:
    """Private/internal API response generator.

    Query redis for a named queue, and return the last `count` messages from that queue.
    Messages are deleted from the queue (via .pop()) as they are retrieved.

    If the the value of an element on the queue is the string mqueue.QUEUE_EXHAUSTED
    this view will return http 286, which tells htmx to stop polling.

    Args:
        queue_name: Required queue name
        item_template: optional template file location for rendering each row item
    Query params:
        count: Optional number of messages to retrieve "per gulp"
        index: Starting point from the queue (i.e. how many messages retrieved so far)

    Returns:
        Last `n` messages in the queue formatted in an html snippet (each rendered by the item_template)
    """
    mode = request.GET.get("mode", "")
    start = int(request.GET.get("index", 0))
    end = start + int(request.GET.get("count", 5))
    if mode == "replace":
        # get the last item only
        start = end = -1
    mqueue = get_rt_queue_handle(queue_name)

    items = list()
    status_code = 200
    for temp_obj in mqueue.range(start, end):
        # If sender tells us the queue is done, return 286
        # which instructs htmx to stop polling
        if temp_obj == mqueue.QUEUE_EXHAUSTED:
            status_code = 286
            # replace always replaces innerHTML, so make sure we've got at least one item
            if mode == "replace" and not items:
                # only one, but we're getting a list back
                for last_val in mqueue.range(-2, -2):
                    items.append(last_val)
            break

        if temp_obj:
            items.append(temp_obj)

    if not items and status_code == 200:
        return HttpResponse("", status=204)  # no content, not exhausted

    if mode == "reverse":
        items.reverse()

    try:
        body = "".join(loader.render_to_string(item_template, {"item": item}) for item in items)
    except TemplateDoesNotExist:
        body = "template not found"
        status_code = 286
    return HttpResponse(body, status=status_code)
