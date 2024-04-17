import asyncio
import logging
from contextlib import suppress

logger = logging.getLogger(__name__)


def drain(q: asyncio.Queue):
    with suppress(asyncio.QueueEmpty):
        # drain
        while True:
            q.get_nowait()
            q.task_done()


def enqueue(queue: asyncio.Queue, msg):
    while True:
        try:
            queue.put_nowait(msg)
            return
        except asyncio.QueueFull:
            # discard
            logger.warning(f"discard msg:{msg}")
            with suppress(asyncio.QueueEmpty):
                queue.get_nowait()
