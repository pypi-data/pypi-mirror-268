import logging
import time
from contextlib import contextmanager
from queue import Queue
from threading import Thread

log = logging.getLogger(__name__)


@contextmanager
def poll2queue(func, step=60, queue=None):
    if not queue:
        queue = Queue()
    stop = False

    def target():
        nonlocal queue
        nonlocal stop
        while not stop:
            try:
                res = func()
                log.debug(f"Result: {res}")
                queue.put(res)
            except Exception as e:
                log.error(f"Exception: {e}")
            time.sleep(step)

    th = Thread(target=target)
    try:
        th.start()
        yield queue
    finally:
        stop = True
        th.join()


def poll(func, step=60):
    queue = Queue()
    with poll2queue(func, step=step, queue=queue) as q:
        while True:
            yield q.get()
