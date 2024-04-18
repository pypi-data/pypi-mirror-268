from persona_ai.domain import roles
from persona_ai.domain.conversations import Message
from persona_ai.personas.base import Persona
from persona_ai.transport.messagebus import MessageBus


class TerminalUserProxy(Persona):
    """
    Terminal user is a persona that can send messages to the terminal.
    """

    def __init__(
        self,
        message_bus: MessageBus = None,
    ):
        super().__init__(
            name="Terminal",
            role=roles.USER,
            scope="Terminal user",
            message_bus=message_bus,
            allow_broadcasting=True,
            included_in_moderation=False,
        )

    def receive(self, message: Message, **kwargs):
        print("{}: {}".format(message.sender_name, message.get_text()))
