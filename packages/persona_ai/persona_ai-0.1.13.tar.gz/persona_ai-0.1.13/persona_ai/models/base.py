from abc import ABC, abstractmethod
from typing import Union, List

from persona_ai.domain.conversations import Message, MessageBody
from persona_ai.tools.base import ToolDefinition


class Chat(ABC):
    """
    Represents a chat session with a model.
    """

    @abstractmethod
    def send_message(self, content: List[Message], **kwargs) -> MessageBody:
        pass


class GenAIModel(ABC):
    """
    Represents a generic AI model.
    """

    @abstractmethod
    def generate(
        self,
        contents: Union[str, Message, List[Message]],
        tools: List[ToolDefinition] = None,
        **kwargs
    ) -> MessageBody:
        pass

    @property
    def is_chat_supported(self):
        return False

    def start_chat(self, history: List[Message] = None, **kwargs) -> Chat:
        raise NotImplementedError("Chat is not supported by this model.")
