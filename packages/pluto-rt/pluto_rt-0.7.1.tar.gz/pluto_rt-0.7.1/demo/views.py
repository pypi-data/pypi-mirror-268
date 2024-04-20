import uuid

from django.shortcuts import render

from .tasks import sample_ops_function, sample_progress_function


def demo_index(request):
    """
    Lists the various demos
    """
    return render(request, "demo/demo_index.html")


def demo_list(request):
    """
    Real-time list results display of demo report run
    """
    # come up with a unique-ish queue name. it shouldn't be possible to
    # replicate it by another user (it shouldnt' use a timestamp alone)
    queue_name = f"listqueue_{uuid.uuid4()}"

    # kick off the long running task, passing it the unique queue name
    sample_ops_function.delay(queue_name)

    # pass on the queue name to the results view
    ctx = {
        "queue_name": queue_name,
        # these are optional, for polling only
        "num_per_gulp": 100,
        "interval_seconds": 3,
    }
    # "reverse" causes new results to be displayed at the top of the page, not bottom.
    # "replace" just replaces the content
    # This can also be passed in to the template using an "include" variable
    ctx["mode"] = request.GET.get("mode", "normal")

    # use polling instead of SSE
    if request.GET.get("polling"):
        ctx["polling"] = True

    return render(request, "demo/demo_list.html", ctx)


def demo_messages(request):
    """
    Real-time message popup display
    """
    queue_name = f"messagequeue_{uuid.uuid4()}"
    sample_ops_function.delay(queue_name)
    ctx = {"queue_name": queue_name}
    # use polling instead of SSE
    if request.GET.get("polling"):
        ctx["polling"] = True
    return render(request, "demo/demo_messages.html", ctx)


def demo_progress(request):
    """Progress bar display"""
    queue_name = f"messagequeue_{uuid.uuid4()}"
    sample_progress_function.delay(queue_name)
    ctx = {"queue_name": queue_name}
    # use polling instead of SSE
    if request.GET.get("polling"):
        ctx["polling"] = True
    return render(request, "demo/demo_progress.html", ctx)
