from abc import ABC, abstractmethod


class CodeRunner(ABC):
    """
    Base class for code runners.
    Code runners are used from Coders to run code snippets.

    Example:
    ```python
    class MyCodeRunner(CodeRunner):
        def run(self, code: str, timeout: int = None) -> Result:
            # run the code and return the result
            pass
    ```
    """

    class Result:
        """
        Result of the code execution.

        Attributes:
        - success: bool, whether the code was executed successfully.
        - code: str, the code that was executed.
        - output: dict, the output of the code execution.
        - error: Exception, the error that occurred during the code execution.

        Example:
        ```python
        result = MyCodeRunner.Result(success=True, code="print('Hello, World!')", output={"stdout": "Hello, World!\n"})
        ```

        """

        def __init__(
            self, success, code: str, output: dict = None, error: Exception = None
        ):
            self.success = success
            self.code = code
            self.output = output
            self.error = error

    @abstractmethod
    def run(self, code: str, timeout: int = None) -> Result:
        pass
