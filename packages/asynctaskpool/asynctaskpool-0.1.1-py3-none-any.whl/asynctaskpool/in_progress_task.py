import asyncio
import logging
from typing import Any, Coroutine


class TaskpoolTask:
    _logger = logging.getLogger(__name__)
    _no_result_yet = object()

    def __init__(self, task_id: object, future: Coroutine):
        self._event = asyncio.Event()
        self._task_id = task_id
        self._future = future
        self._task_result = self._no_result_yet

    async def wait_and_get_result(self) -> Any:
        self._logger.debug("Task %s in progress. Waiting.", self._task_id)
        await self._event.wait()
        self._logger.debug("Finished waiting for %s.", self._task_id)

        return self._task_result

    async def run_task(self) -> Any:
        self._task_result = await self._future
        return self._task_result

    def mark_finished(self):
        self._event.set()

    @property
    def task_id(self):
        return self._task_id

    @property
    def task_result(self):
        if not self._has_result():
            raise RuntimeError("Task does not have a result yet")
        else:
            return self._task_result

    def _has_result(self):
        return self._task_result is not self._no_result_yet
