import json
import logging
import multiprocessing
import sys
from io import StringIO
from typing import Dict, Optional

from persona_ai.code_runners.base import CodeRunner

logger = logging.getLogger()


class LocalCodeRunner(CodeRunner):
    """
    Executes Python code on local machine.

    Example:
    ```python
    code_runner = LocalCodeRunner()
    result = code_runner.run("print('Hello, World!')")
    print(result.output)
    ```
    """

    globals: dict = {}
    """
    Global variables that are available to the code snippets.
    """

    locals: dict = {}
    """
    Local variables that are available to the code snippets.
    """

    def _run(
        self,
        code: str,
        globals: Optional[Dict],
        locals: Optional[Dict],
        queue: multiprocessing.Queue,
    ) -> None:
        string_stdout = StringIO()
        old_stdout = sys.stdout
        sys.stdout = string_stdout
        try:
            exec(code, globals, locals)
            value = string_stdout.getvalue()
            output: dict
            try:
                output = json.loads(value)
            except json.JSONDecodeError:
                output = {"message": value}

            queue.put(
                CodeRunner.Result(success=True, code=code, output=output, error=None)
            )
        except Exception as e:
            queue.put(CodeRunner.Result(success=False, code=code, output=None, error=e))
        finally:
            sys.stdout = old_stdout

    def run(self, code: str, timeout: int = None) -> CodeRunner.Result:
        """Run Python code in a separate process."""

        queue = multiprocessing.Queue()

        logger.debug("Running python code: {}".format(code))

        if timeout is not None:
            # create a Process
            p = multiprocessing.Process(
                target=self._run, args=(code, self.globals, self.locals, queue)
            )

            p.start()
            p.join(timeout)

            if p.is_alive():
                p.terminate()
                return CodeRunner.Result(
                    success=False, code=code, output=None, error=TimeoutError()
                )
        else:
            self._run(code, self.globals, self.locals, queue)

        result = queue.get()

        logger.debug("Code runner output: {}".format(result.output))

        return result
