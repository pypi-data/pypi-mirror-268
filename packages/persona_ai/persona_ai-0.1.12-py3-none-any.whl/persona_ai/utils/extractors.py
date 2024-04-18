import re

from strip_markdown import strip_markdown


def extract_json(data: str) -> str:
    """Extract JSON delimited from ```json ... ``` from a string."""

    data = data.strip()
    if data.startswith("{") and data.endswith("}"):
        return data

    json = re.search(r"```json(.*?)```", data, re.DOTALL)
    if json:
        return json.group(1)


def extract_json_object(data: str) -> str:
    """Extract JSON object delimited a string."""

    start_index = data.find("{")
    end_index = data.rfind("}") + 1
    return data[start_index:end_index]


def extract_moderation_block(data: str) -> str:
    """Extract moderation block delimited from ```moderation ... ``` from a string."""

    python = re.search(r"```moderation(.*?)```", data, re.DOTALL)
    if python:
        return python.group(1)
    else:
        return data


def extract_python_code(data: str) -> str:
    """Extract Python code delimited from ```python ... ``` from a string."""
    python = re.search(r"```python(.*?)```", data, re.DOTALL)
    if python:
        return python.group(1)


def markdown_to_text(markdown: str) -> str:
    """Convert markdown to text."""
    return strip_markdown(markdown)
