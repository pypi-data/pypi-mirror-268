from abc import ABC, abstractmethod
from typing import List

from persona_ai.domain.conversations import ToolSuggestion
from persona_ai.tools.base import ToolDefinition


class ToolManager(ABC):
    """This is the tool manager base class. A technician uses this class to manage and execute tools."""

    tool_definitions: List[ToolDefinition] = []
    """Tool definitions."""

    def __init__(self, tool_definitions: List[ToolDefinition]):
        self.tool_definitions = tool_definitions

    def get_tool_definitions(self) -> List[ToolDefinition]:
        return self.tool_definitions

    @abstractmethod
    def execute(self, tool_suggestion: ToolSuggestion):
        """Execute a tool."""
        raise NotImplementedError
