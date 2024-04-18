from jinja2 import (
    Environment,
    select_autoescape,
    PackageLoader,
    BaseLoader,
)

from persona_ai.prompts.base import Prompt


class JinjaTemplatePrompt(Prompt):
    """
    Jinja template prompt.
    This prompt uses Jinja2 template to render a prompt.
    Template is a file with .jinja2 extension and can be loaded from a package or a file system.
    Default base loader uses persona_ai package and prompt_templates directory.
    Specify a BaseLoader to load templates from a file system.

    Example:
    ```python
    prompt = JinjaTemplatePrompt(template="assistant", name="Alice")
    rendered_prompt = prompt.render()
    ```

    """

    def __init__(self, template: str, loader: BaseLoader = None, **kwargs):
        self.environment = Environment(
            loader=(
                loader if loader else PackageLoader("persona_ai", "prompt_templates")
            ),
            autoescape=select_autoescape(),
        )
        self.template = template
        self.kwargs = kwargs

    def render(self, **kwargs) -> str:
        template = self.environment.get_template(
            f"{self.template}.jinja2", globals=None
        )
        return template.render(**self.kwargs, **kwargs)


class JinjaTextPrompt(Prompt):
    """
    Jinja text prompt.
    This prompt uses Jinja2 template to render a prompt.
    Compared to JinjaTemplatePrompt, this prompt uses a text as a template.
    Text should be specified in the constructor.

    Example:
    ```python
    prompt = JinjaTextPrompt("Hello, {{ name }}!")
    rendered_prompt = prompt.render(name="Alice")
    ```
    """

    def __init__(self, prompt_text: str, loader: BaseLoader = None, **kwargs):
        self.environment = Environment(
            loader=(
                loader if loader else PackageLoader("persona_ai", "prompt_templates")
            ),
            autoescape=select_autoescape(),
        )
        self.prompt_text = prompt_text
        self.kwargs = kwargs

    def render(self, **kwargs) -> str:
        template = self.environment.from_string(
            source=self.prompt_text, globals=None, template_class=None
        )
        return template.render(**self.kwargs, **kwargs)
