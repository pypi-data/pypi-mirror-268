import base64
import time
from typing import List, Any

from pydantic import BaseModel

from persona_ai.domain.utils import create_id


class ToolSuggestion(BaseModel):
    """Message body tool suggestion model.

    This model body tool suggestion that must be executed by tool server.
    """

    suggested_tool: str | None
    """Tool name."""

    input: dict | None
    """Tool input."""


class ToolOutput(BaseModel):
    """Message body tool output model.

    This model body tool output that must be executed by tool server.
    """

    suggestion: ToolSuggestion
    """Tool suggestion that originate this output."""

    output: dict[str, Any] | None
    """Tool output."""


class CodeRunnerOutput(BaseModel):
    """
    Code runner output model.
    """

    success: bool
    """Flag to indicate if code execution was successful."""

    code: str
    """Executed code."""


class Source(BaseModel):
    """Source.

    This model represents the source of retrieved text
    """

    url: str
    """Source url."""


class Blob(BaseModel):
    """Message body bloc.

    This model represents a blob in a message.
    """

    id: str
    """Blob identifier"""

    base64_data: str
    """Image base64 data in string format"""

    content_type: str
    """Image content type"""


class MessageBody(BaseModel):
    """Message body model.

    This model represents a message body.
    """

    text: str | None = None
    """Message text"""

    blobs: List[Blob] | None = None
    """Message blobs"""

    tool_suggestion: ToolSuggestion | None = None
    """A tool suggested by a technician"""

    tool_output: ToolOutput | None = None
    """A tool output by a technician that executes a tool suggestion."""

    sources: List[Source] | None = None
    """Message sources"""

    code_runner_output: CodeRunnerOutput | None = None
    """Code runner output"""

    @staticmethod
    def clone(body: "MessageBody") -> "MessageBody":
        return MessageBody(
            text=body.text,
            blobs=body.blobs,
            tool_suggestion=body.tool_suggestion,
            tool_output=body.tool_output,
            sources=body.sources,
            code_runner_output=body.code_runner_output,
        )


class Message(BaseModel):
    """Message model.

    This model represents a message.
    """

    id: str
    """Message id"""

    conversation_id: str
    """Parent conversation id"""

    sender_id: str
    """User id"""

    sender_name: str
    """The name of personas that sent the message."""

    sender_role: str
    """The role of personas that sent the message."""

    body: MessageBody
    """Message text"""

    timestamp: float = time.time()
    """Message timestamp"""

    reply: bool = True
    """Flag to indicate if message require a reply"""

    reply_to: str | None = None
    """Participant id to reply to. If none is specified, sender_id will be used"""

    received: bool = False
    """Flag to indicate if message was received by recipient"""

    is_termination_message: bool = False
    """Flag to indicate if message is a termination message"""

    @property
    def is_text(self) -> bool:
        return self.body.text is not None

    @property
    def is_tool_output(self) -> bool:
        return self.body.tool_output is not None

    @property
    def is_tool_suggestion(self) -> bool:
        return self.body.tool_suggestion is not None

    def get_text(self) -> str:
        if self.body is None:
            return ""

        if self.body.text is None and self.body.tool_output is not None:
            return f"""I've used this tool: {self.body.tool_output.suggestion.suggested_tool}. Result is ```{self.body.tool_output.output}```"""

        if self.body.blobs:
            for blob in self.body.blobs:
                blobs = []
                if blob.content_type == "text/plain":
                    decoded = base64.b64decode(blob.base64_data).decode("utf-8")
                    blobs.append(f"{blob.id}\n{decoded}")

                return "\n\n".join(blobs)

        return self.body.text

    def __str__(self):
        return self.get_text()

    def mark_as_received(self):
        self.received = True

    def to_conversational(self) -> str:
        return f"{self.sender_name} -> {self.get_text().strip()}"


class Conversation(BaseModel):
    """Conversation model.

    This model represents a conversation.
    """

    id: str
    """Conversation id"""

    title: str | None = None
    """Conversation title"""

    summary: str | None = None
    """Conversation summary"""


def create_message(
    body: MessageBody,
    conversation_id: str,
    sender_id: str,
    sender_name: str,
    sender_role: str,
    is_termination_message: bool = False,
):
    """Create a text message."""
    return Message(
        id=create_id(prefix="msg"),
        conversation_id=conversation_id,
        sender_id=sender_id,
        sender_name=sender_name,
        sender_role=sender_role,
        body=body,
        is_termination_message=is_termination_message,
    )


def create_text_message(
    text: str, conversation_id: str, sender_id: str, sender_name: str, sender_role: str
):
    """Create a text message."""
    return Message(
        id=create_id(prefix="msg"),
        conversation_id=conversation_id,
        sender_id=sender_id,
        sender_name=sender_name,
        sender_role=sender_role,
        body=MessageBody(text=text),
    )


def create_blobs_message(
    text: str,
    blobs: List[Blob],
    conversation_id: str,
    sender_id: str,
    sender_name: str,
    sender_role: str,
):
    """Create a images message."""
    return Message(
        id=create_id(prefix="msg"),
        conversation_id=conversation_id,
        sender_id=sender_id,
        sender_name=sender_name,
        sender_role=sender_role,
        body=MessageBody(text=text, blobs=blobs),
    )


def create_tool_suggestion_message(
    text: str,
    tool_suggestion: ToolSuggestion,
    conversation_id: str,
    sender_id: str,
    sender_name: str,
    sender_role: str,
):
    """Create a tool suggestion message."""
    return Message(
        id=create_id(prefix="msg"),
        conversation_id=conversation_id,
        sender_id=sender_id,
        sender_name=sender_name,
        sender_role=sender_role,
        body=MessageBody(text=text, tool_suggestion=tool_suggestion),
    )
