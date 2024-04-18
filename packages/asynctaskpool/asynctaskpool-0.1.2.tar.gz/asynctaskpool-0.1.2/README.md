# AsyncTaskPool

This tool provides an asynchronous 'task pool'. Tasks with an identifier can be submitted to it and they will only be executed once -
even when submitted again before the first task has finished.
The results of these tasks will be cached for next time.