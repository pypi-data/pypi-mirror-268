import asyncio
import logging
from typing import TypeVar, Generic, Any, Coroutine

from .in_progress_task import TaskpoolTask

T = TypeVar("T")


class AsyncTaskPool(Generic[T]):
    """
    A TaskPool is a utility that receives submitted tasks which have an identity and which should be executed no more
    than once, even in parallel.
    """

    _logger = logging.getLogger(__name__)

    def __init__(self, restart_if_finished: bool = False):
        self._task_tracker: dict[object, asyncio.Event | T | None] = {}
        self._semaphore = asyncio.Semaphore()
        self._restart_task_if_finished: bool = restart_if_finished

    def take_in_precomputed_result_map(self, results: dict[object, T]) -> None:
        self._task_tracker.update(**results)

    async def submit_new_task(self, task_id: object, future: Coroutine) -> T | None:
        # Any async item that we need to await is put into this.
        # Then we await it at the end of the function, so we can use exception-safe 'with' block without holding the semaphore too long.
        async_operation_to_wait_for: Coroutine | None = None

        async with self._semaphore:
            if self._has_task_been_submitted_yet(task_id):
                task = self._get_tracked_task(task_id)

                if not self._is_task_in_progress(task):
                    if not self._restart_task_if_finished:
                        self._logger.debug("Task %s already finished, returning.", task_id)
                        return task
                    else:
                        async_operation_to_wait_for = self._create_and_run_task(task_id, future)
                else:
                    async_operation_to_wait_for = task.wait_and_get_result()
            else:
                async_operation_to_wait_for = self._create_and_run_task(task_id, future)

        if async_operation_to_wait_for is not None:
            return await async_operation_to_wait_for

    def _has_task_been_submitted_yet(self, task_id: object):
        return task_id in self._task_tracker.keys()

    def _get_tracked_task(self, task_id: object) -> TaskpoolTask | T | None:
        return self._task_tracker[task_id]

    @staticmethod
    def _is_task_in_progress(task: Any) -> bool:
        return isinstance(task, TaskpoolTask)

    def _create_and_track_new_unstarted_task(self, task_id: object, future: Coroutine) -> TaskpoolTask:
        self._logger.debug("Creating new task %s.", task_id)

        new_in_progress_task = TaskpoolTask(task_id=task_id, future=future)
        self._track_new_task(new_in_progress_task)
        return new_in_progress_task

    def _track_new_task(self, task: TaskpoolTask):
        self._task_tracker[task.task_id] = task

    async def _run_task_and_record_result(self, task: TaskpoolTask) -> T:
        task_result = await task.run_task()

        self._logger.debug("Task %s finished", task.task_id)
        await self._record_result_of_task_and_mark_finished(task=task, result=task_result)

        return task_result

    async def _record_result_of_task_and_mark_finished(self, task: TaskpoolTask, result: Any):
        async with self._semaphore:
            self._update_tracked_task_with_result(task.task_id, result)

        task.mark_finished()

    def _update_tracked_task_with_result(self, task_id: object, result: Any):
        self._task_tracker[task_id] = result

    async def _create_and_run_task(self, task_id: object, future: Coroutine):
        new_task = self._create_and_track_new_unstarted_task(task_id=task_id, future=future)
        return await self._run_task_and_record_result(new_task)

    def clear_results(self) -> None:
        self._task_tracker.clear()

    def get_results_of_all_completed_tasks(self) -> list[T]:
        def exclude_none_and_unfinished_tasks(it):
            return it is not None and not self._is_task_in_progress(it)

        return list(filter(exclude_none_and_unfinished_tasks, self._task_tracker.values()))
