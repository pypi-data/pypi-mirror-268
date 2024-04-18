from persona_ai.prompts.base import Prompt


class TextPrompt(Prompt):
    """
    Text prompt.
    This prompt uses a text as a template.
    Text should be specified in the constructor.
    It uses python str.format() method to render the prompt.

    Example:
    ```python
    prompt = TextPrompt("Hello, {name}!")
    rendered_prompt = prompt.render(name="Alice")
    ```
    """

    def __init__(self, prompt: str, **kwargs):
        self.prompt = prompt
        self.kwargs = kwargs

    def render(self, **kwargs) -> str:
        return self.prompt.format(self.kwargs, **kwargs)
