from typing import Any


class ToolDefinition:
    """Represents a tool definition used by llm to make a suggestion."""

    name: str
    """Tool name."""

    description: str
    """Tool description to permit LLM to identify the tool."""

    schema: dict[str, Any]
    """Tool input schema."""

    def __init__(self, name: str, description: str, schema: dict[str, Any]):
        self.name = name
        self.description = description
        self.schema = schema
