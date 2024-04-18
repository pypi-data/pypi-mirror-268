import logging
from typing import List, Any

from persona_ai.domain.conversations import ToolSuggestion
from persona_ai.tools.base import ToolDefinition
from persona_ai.tools.manager import ToolManager


class FunctionalTool(ToolDefinition):
    """Represents a functional tool that can be executed by a local tool manager."""

    name: str
    """Tool name."""

    function: callable
    """Tool function."""

    def __init__(
        self,
        name: str,
        description: str,
        schema: dict[str, Any],
        function: callable,
    ):
        super().__init__(name, description, schema)
        self.function = function


class FunctionalToolManager(ToolManager):
    """
    This is the functional tool manager class.
    A technician uses this class to manage and execute functional tools.
    """

    def __init__(self, tools: List[FunctionalTool]):
        super().__init__(tool_definitions=tools)

    def execute(self, tool_suggestion: ToolSuggestion) -> dict:
        """
        Execute a functional tool.
        """

        tool = next(
            (
                t
                for t in self.get_tool_definitions()
                if t.name == tool_suggestion.suggested_tool
            ),
            None,
        )

        if tool is None:
            raise ValueError(f"Tool not found: {tool_suggestion.suggested_tool}")

        # tool must be an instance of FunctionalTool
        if not isinstance(tool, FunctionalTool):
            raise ValueError(f"Invalid tool type: {type(tool)}")

        output = tool.function(tool_suggestion.input)

        logging.debug(f"Executed tool: {tool.name} with input: {tool_suggestion.input}")
        logging.debug(f"Output: {output}")

        return output
