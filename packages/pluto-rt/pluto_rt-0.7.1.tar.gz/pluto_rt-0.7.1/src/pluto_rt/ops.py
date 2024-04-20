import pickle
import time

from django.conf import settings
from django_redis import get_redis_connection


class Queue:
    """A simple implementation of message queuing in redis.
    We can't push python data structures directly into redis -
    must pickle to push and unpickle to retrieve.
    """

    QUEUE_EXHAUSTED = '"_queue_exhausted_"'

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.redis = get_redis_connection("default")

    def complete(self, clear_delay: int = 5):
        """Mark the queue as complete, wait a few seconds and then purge the queue
        purging can be skipped if clear_delay is 0
        """
        self.push(self.QUEUE_EXHAUSTED)
        if clear_delay:
            time.sleep(clear_delay)
            self.redis.delete(self.name)

    def push(self, message: dict):
        message = pickle.dumps(message)
        self.redis.rpush(self.name, message)

    def pop(self) -> dict | None:
        raw_message = self.redis.lpop(self.name)
        if raw_message:
            message = pickle.loads(raw_message)
            return message

        return None

    def range(self, start: int, end: int) -> list[dict]:
        """Return from the list, but don't pop
        This is useful for long running processes where the caller remembers
        the index number and can re-fetch the queue (i.e. have multiple consumers).

        start and end can be negative and are fetched from the end of the list
        """
        return [pickle.loads(msg) for msg in self.redis.lrange(self.name, start, end)]


def get_rt_queue_handle(queue_name: str) -> Queue:
    """Get a handle on a redis message queueing connection, for reading or writing.

    Queue name should include a function descriptor and ID like "equipment_upload_357"
    """
    prefix = settings.CACHES["default"].get("KEY_PREFIX", "default")
    return Queue(f"{prefix}_{queue_name}")
