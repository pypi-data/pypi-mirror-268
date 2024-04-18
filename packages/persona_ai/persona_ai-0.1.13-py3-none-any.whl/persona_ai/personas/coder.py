from persona_ai.code_runners.base import CodeRunner
from persona_ai.code_runners.local import LocalCodeRunner
from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain.conversations import MessageBody, Message, CodeRunnerOutput
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.personas.assistant import Assistant
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.jinja import JinjaTemplatePrompt
from persona_ai.transport.messagebus import MessageBus
from persona_ai.utils.extractors import extract_python_code


def extract_text(text):
    """
    Coder generate python code and append text at the end after closing token ```.
    This function extract that text.
    """
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "```":
            return "\n".join(lines[i + 1 :])
    return ""


def _normalize_blobs(output: dict):
    blobs = output["blobs"] if "blobs" in output else None
    if blobs is None:
        return

    if not isinstance(blobs, list):
        return

    for blob in blobs:
        blob["base64_data"] = str(blob["base64_data"])


class Coder(Assistant):
    """
    Coder is a persona that can generate python code based on the input it receives.
    The generated code is executed by a CodeRunner.
    """

    code_runner: CodeRunner
    """
    Code runner used by the coder to run the code.
    """

    code_generation_instructions: str
    """
    Instructions for code generation.
    """

    def __init__(
        self,
        name: str,
        role: str,
        scope: str,
        id: str = None,
        code_runner: CodeRunner = None,
        model: GenAIModel = None,
        message_bus: MessageBus = None,
        conversation_manager: ConversationManager = None,
        prompt: Prompt = None,
        code_generation_instructions: str = None,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
        can_reply_multiple_times: bool = False,
    ):
        super().__init__(
            id=id if id else create_id(prefix="coder"),
            name=name,
            role=role,
            scope=scope,
            model=model if model else PersonaAI.coder_model,
            message_bus=message_bus,
            prompt=prompt if prompt else JinjaTemplatePrompt(template="coder"),
            conversation_manager=conversation_manager,
            allow_broadcasting=allow_broadcasting,
            included_in_moderation=included_in_moderation,
            can_reply_multiple_times=can_reply_multiple_times,
        )

        self.code_runner = code_runner if code_runner else LocalCodeRunner()
        self.code_generation_instructions = code_generation_instructions

    def _render_template_prompt(self, history, message):
        return self.prompt.render(
            conversation_history=history,
            request=message,
            code_generation_instructions=self.code_generation_instructions,
        )

    def _generate_reply(self, body: MessageBody, request: Message) -> Message:
        message = super()._generate_reply(body, request)

        if message.body.text is not None:
            code = extract_python_code(message.body.text)
            result = self.code_runner.run(code)

            if not result.success:
                message.body.text = repr(result.error)
            else:
                _normalize_blobs(result.output)
                message.body = MessageBody.model_validate(result.output)

            message.body.code_runner_output = CodeRunnerOutput(
                code=code,
                success=result.success,
            )

        return message
