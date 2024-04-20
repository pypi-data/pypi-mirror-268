import random
import time

from celery import Celery
from django.conf import settings
from faker import Faker
from pluto_rt.ops import get_rt_queue_handle

app = Celery("tasks", broker=settings.CACHES["default"]["LOCATION"])


@app.task
def sample_ops_function(queue_name: str, msg_count: int = 25):
    """
    Demo function that processes data, such as reading and
    handling rows of an ETL job (reading a spreadsheet, sending email, whatever.)
    In this case, we just generate `n` random messages and put them
    on the queue. The html template is responsible for popping those
    messages off the queue. In real-world use, this function would be some
    long-running ETL or other task that can be reasonably chunked.

    """
    mqueue = get_rt_queue_handle(queue_name)
    mqueue.push({"status": "info", "msg": "Demo starting"})

    for idx in range(msg_count):
        # Do some work here, on a row or any task chunk, then emit a message

        msg = f"{idx + 1}: {Faker().sentence()}"
        statuses = ["success", "danger", "info", "warning"]

        row_dict = {"status": random.choice(statuses), "msg": msg}
        mqueue.push(row_dict)
        # mimic a long running task
        time.sleep(random.randint(0, 2))

    row_dict = {"status": "success", "msg": "Demo complete"}
    mqueue.push(row_dict)
    mqueue.complete()


@app.task
def sample_progress_function(queue_name: str, msg_count: int = 25):
    """Showing progress"""
    mqueue = get_rt_queue_handle(queue_name)
    value = 0
    while value < msg_count:
        # Do some work here, on a row or any task chunk, then emit a message
        value = min(msg_count, value + random.randint(0, 3))
        mqueue.push({"value": value, "max": msg_count, "percent": f"{value/msg_count:.0%}"})
        # mimic a long running task
        time.sleep(random.randint(0, 2))
    mqueue.complete()
