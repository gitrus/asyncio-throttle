import asyncio
import time
from collections import deque
from typing import Deque


class Throttler:
    def __init__(
        self, rate_limit: int, period: float = 1.0, retry_interval: float = 0.01
    ):
        self.rate_limit = rate_limit
        self.period = period
        self.retry_interval = retry_interval

        self._task_logs: Deque = deque()

    def flush(self) -> None:
        now = time.monotonic()
        while self._task_logs:
            if now - self._task_logs[0] > self.period:
                self._task_logs.popleft()
            else:
                break

    async def acquire(self) -> None:
        while True:
            self.flush()
            if len(self._task_logs) < self.rate_limit:
                break
            await asyncio.sleep(self.retry_interval)

        self._task_logs.append(time.monotonic())

    async def __aenter__(self) -> None:
        await self.acquire()

    async def __aexit__(self, exc_type, exc, tb) -> None:
        pass
