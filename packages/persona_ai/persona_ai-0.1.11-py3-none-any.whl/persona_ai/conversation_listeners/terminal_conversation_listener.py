import base64
import io
import os
import tempfile

from PIL import Image
from termcolor import cprint

from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain import events
from persona_ai.domain.conversations import Message, Blob
from persona_ai.domain.events import Event
from persona_ai.domain.tasks import TaskStatus
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.task_manager.base import TaskManager
from persona_ai.transport.messagebus import ConversationListener
from persona_ai.utils.extractors import markdown_to_text

LINE = "-----------------------------------------------------------"


class TerminalConversationListener(ConversationListener):
    """
    A conversation listener that prints messages and events to the terminal.

    Attributes:
    - conversation_manager: ConversationManager, the conversation manager.
    - task_manager: TaskManager, the task manager.

    Example:
    ```python
    listener = TerminalConversationListener("Terminal", "conversation_id")
    message_bus.register(listener)
    ```
    """

    def __init__(
        self,
        name: str,
        conversation_id: str,
        id: str = None,
        conversation_manager: ConversationManager = None,
        task_manager: TaskManager = None,
    ):
        super().__init__(name, conversation_id, id=id)
        self.conversation_manager = (
            conversation_manager
            if conversation_manager
            else PersonaAI.conversation_manager
        )
        self.task_manager = (
            task_manager if task_manager else TaskManager(PersonaAI.tasks_repository)
        )

    def receive(self, message: Message, **kwargs):
        super().receive(message, **kwargs)

        self._print_message(message)

    def handle_event(self, event: Event, **kwargs):
        super().handle_event(event, **kwargs)
        match event.type:
            case events.ITERATION:
                self._print_iteration(event)
            case events.AGENT_STEP:
                self._print_agent_step(event)

    def _print_agent_step(self, event: Event):
        # event body schema
        # {
        #     "agent_id": self.id,
        #     "conversation_id": message.conversation_id,
        #     "tool_suggestion": fc_message.body.tool_suggestion,
        #     "output": message,
        # }

        cprint(LINE, "white")
        cprint("Agent step", "light_blue")
        cprint(f"Agent: {event.body['agent_id']}", "light_blue")
        cprint(f"Conversation: {event.body['conversation_id']}", "light_blue")
        cprint(f"Tool suggestion: {event.body['tool_suggestion']}", "light_blue")
        cprint(f"Tool Output: {event.body['tool_output']}", "light_blue")
        print()

    def _print_message(self, message: Message):
        print()
        cprint(f"Message from {message.sender_name}", "yellow")

        if message.body.blobs is not None:
            for blob in message.body.blobs:
                self._print_blob(blob)

        text = markdown_to_text(message.get_text())
        cprint(f"{text}", "white")
        print()

    def _print_iteration(self, event: Event):
        cprint(LINE, "white")
        task = self.task_manager.get_by_id(event.body["task_id"])
        if task is None:
            cprint(" *** Task not found *** ", "red")

        if len(task.iterations) == 1 and task.status == TaskStatus.PENDING:
            cprint("Started new task: {}".format(task.id), "light_blue")
            print("")
        else:
            cprint("*** Task status: {}".format(task.status), "light_blue")
            cprint(
                "*** Number of iterations: {}".format(len(task.iterations)),
                "light_grey",
            )
            print()

        moderation_result = event.body["moderation_result"]

        if (
            moderation_result["next"] is None
            and not task.status == TaskStatus.COMPLETED
        ):
            cprint("*** Warning: No next participant found", "light_red")
            print()
        elif not task.status == TaskStatus.COMPLETED:
            cprint(
                "*** Selected participant: {}".format(moderation_result["next"]),
                "light_cyan",
            )
            cprint(
                "*** Reason: {}".format(moderation_result["reason"]),
                "light_cyan",
            )
        if moderation_result["request"]:
            cprint(
                "*** Request: {}".format(moderation_result["request"]),
                "light_cyan",
            )

        if moderation_result["final_answer"]:
            cprint(
                "*** Final answer: {}".format(moderation_result["final_answer"]),
                "light_cyan",
            )

        print()

        if task.status == TaskStatus.FAILED:
            cprint("Task finished with error", "light_red")
        elif task.status == TaskStatus.COMPLETED:
            cprint("Task finished successfully", "green")

        print()

    def _print_blob(self, blob: Blob):
        cprint(f"Blob: {blob.id}", "light_magenta")
        cprint(f"Content Type: {blob.content_type}", "light_magenta")

        if blob.content_type == "image/png" or blob.content_type == "image/jpeg":
            try:
                self._print_base64_encoded_image(blob.base64_data, blob.content_type)
            except Exception as e:
                cprint(f"Error: {e}", "red")
        elif blob.content_type == "text/plain":
            cprint(f"{blob.base64_data}", "white")

        print()

    def _print_base64_encoded_image(self, base64_data: str, content_type: str):
        import pywhatkit

        image_data = base64.b64decode(base64_data)
        image = Image.open(io.BytesIO(image_data))
        extension = content_type.split("/")[1]
        file_name = create_id(prefix="tmp_image")
        temp_image_path = tempfile.gettempdir() + f"/{file_name}.{extension}"
        image.save(temp_image_path)

        ascii_art = pywhatkit.image_to_ascii_art(temp_image_path)
        print(ascii_art)

        os.remove(temp_image_path)
