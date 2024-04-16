from _typeshed import Incomplete
from types import TracebackType
from typing import Callable

class ScopedTimer:
    '''
    A context manager for profiling code execution time.

    This class measures the execution time of a block of code or function.
    Can be used as a decorator or with a `with` statement.

    :Example:

    ```python
    with ScopedTimer("Some Code"):
        ... # some time-consuming code here

    @ScopedTimer("Some Function")
    def time_consuming_function():
        ... # some time-consuming code here
    ```

    :param reason: A description of the code block or function being timed.
    :param indentation: The number of spaces for indentation in the printed log. Default is 0.
    :param enter_msg: A flag to specify whether to print a message at the start and end of the timer.
    '''
    label: Incomplete
    indentation: Incomplete
    enter_msg: Incomplete
    elapsed_time: float
    def __init__(self, label: str = '', indentation: int = 0, enter_msg: bool = False) -> None: ...
    def __call__(self, func: Callable) -> Callable: ...
    start_time: Incomplete
    def __enter__(self) -> ScopedTimer: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback_: TracebackType | None) -> None: ...
