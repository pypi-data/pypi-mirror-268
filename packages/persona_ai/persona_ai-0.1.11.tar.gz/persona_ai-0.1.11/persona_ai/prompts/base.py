from abc import ABC, abstractmethod


class Prompt(ABC):
    """
    Prompt interface.
    Assistants use prompts to generate messages.
    """

    @abstractmethod
    def render(self, **kwargs) -> str:
        raise NotImplementedError
