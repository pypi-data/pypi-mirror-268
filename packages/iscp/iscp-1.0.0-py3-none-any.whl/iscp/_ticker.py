import asyncio
from contextlib import asynccontextmanager

__all__ = ["Ticker"]


class Ticker(object):
    @classmethod
    @asynccontextmanager
    async def of(cls, delay: float):
        tick = cls(delay)
        try:
            yield tick
        finally:
            tick.stop()

    def __init__(self, delay: float):
        self._delay = delay
        self._stopped = asyncio.Event()
        self._current_tick = asyncio.create_task(asyncio.sleep(self._delay))

    async def __call__(self):
        self._stopped.clear()
        i = 0
        await self._current_tick
        while True:
            if self._stopped.is_set():
                return
            self._current_tick = asyncio.create_task(asyncio.sleep(self._delay))
            yield i
            i += 1
            await self._current_tick

    def stop(self):
        if self._current_tick:
            self._current_tick.cancel()
        self._stopped.set()
