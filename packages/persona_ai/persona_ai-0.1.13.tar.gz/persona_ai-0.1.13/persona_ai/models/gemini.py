import base64
import logging
from typing import Union, List, Iterable

import google
import vertexai
from google.cloud.aiplatform_v1 import FunctionCall
from google.cloud.aiplatform_v1beta1 import FunctionCallingConfig
from vertexai.generative_models import (
    Content,
    Part,
    GenerationResponse,
    HarmCategory,
    HarmBlockThreshold,
    GenerativeModel,
    Tool,
    GenerationConfig,
    FunctionDeclaration,
    ChatSession,
)
from vertexai.generative_models._generative_models import ToolConfig

from persona_ai.domain.conversations import Message, MessageBody, ToolSuggestion
from persona_ai.models.base import GenAIModel, Chat
from persona_ai.tools.base import ToolDefinition

logger = logging.getLogger(__name__)


class GeminiModel(GenAIModel):
    """
    Represents a generative model using the Gemini model.
    """

    model_name = "gemini-pro"
    gemini: GenerativeModel | None
    model_kwargs = {}
    force_function_calling = False
    system_instructions: str = None

    def __init__(
        self,
        service_account: str = None,
        project_id: str = None,
        location: str = None,
        model_name: str = "gemini-pro",
        force_function_calling: bool = False,
        system_instructions: str = None,
        **kwargs,
    ):
        self.service_account = service_account
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.model_kwargs = kwargs
        self.gemini = None
        self.force_function_calling = force_function_calling
        self.system_instructions = system_instructions

    def _init_gemini(self):
        vertexai.init(
            service_account=self.service_account,
            project=self.project_id,
            location=self.location,
        )
        self.gemini = GenerativeModel(
            self.model_name, system_instruction=self.system_instructions
        )

    @property
    def is_chat_supported(self):
        return True

    def start_chat(self, history: List[Message] = None, **kwargs) -> Chat:
        if not self.gemini:
            self._init_gemini()

        gemini_contents = (
            self._prepare_parts(history) if history and len(history) > 0 else None
        )

        chat_session = self.gemini.start_chat(
            history=(
                [Content(role="user", parts=gemini_contents)]
                if gemini_contents
                else None
            )
        )

        logger.debug(f"Chat session started: {chat_session}")

        return GeminiChat(self, chat_session)

    def generate(
        self,
        contents: Union[str, Message, List[Message]],
        tools: List[ToolDefinition] = None,
        **kwargs,
    ) -> MessageBody:
        if not self.gemini:
            self._init_gemini()

        gemini_contents = self._prepare_parts(contents, tools)
        gemini_functions = None
        if tools:
            gemini_functions = self._prepare_functions(tools)

        gemini_tools = None
        if gemini_functions:
            gemini_tools = [
                Tool(
                    function_declarations=gemini_functions,
                )
            ]

        logger.debug(f"Request to gemini: {gemini_contents}, tools: {gemini_tools}")

        tool_config = (
            ToolConfig(
                function_calling_config=ToolConfig.FunctionCallingConfig(
                    mode=ToolConfig.FunctionCallingConfig.Mode.ANY
                )
            )
            if self.force_function_calling
            else None
        )

        response = self.gemini.generate_content(
            contents=gemini_contents,
            tools=gemini_tools,
            generation_config=GenerationConfig(**self.model_kwargs, **kwargs),
            tool_config=tool_config,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            },
        )

        logger.debug(f"Response from gemini: {response}")

        return self._parse_response(response)

    def _prepare_parts(
        self,
        content: Union[str, Message, List[Message]],
        tools: List[ToolDefinition] = None,
    ):
        gemini_parts: List[Part] = []

        if isinstance(content, str):
            gemini_parts.append(Part.from_text(content))
        if isinstance(content, Message):
            gemini_parts.extend(self._prepare_message(content, tools))
        if isinstance(content, list):
            for c in content:
                for m in self._prepare_parts(c, tools):
                    gemini_parts.append(m)

        return gemini_parts

    def _prepare_message(
        self, message: Message, tools: List[ToolDefinition] = None
    ) -> List[Part]:
        parts: List[Part] = []

        if message.body.text:
            parts.append(Part.from_text(message.body.text))

        if message.body.blobs:
            for blob in message.body.blobs:
                if blob.base64_data:
                    decoded_bytes = base64.b64decode(blob.base64_data)
                    parts.append(Part.from_data(decoded_bytes, blob.content_type))
                elif blob.url:
                    parts.append(
                        Part.from_uri(blob.uri, blob.content_type),
                    )

        if message.body.tool_suggestion and (
            tools is None
            or any(
                [
                    tool.name == message.body.tool_suggestion.suggested_tool
                    for tool in tools
                ]
            )
        ):
            parts.append(
                Part.from_dict(
                    {
                        "function_call": {
                            "name": message.body.tool_suggestion.suggested_tool,
                        }
                    }
                )
            )
            role = "model"
        elif message.body.tool_output:
            if tools is None or any(
                [
                    tool.name == message.body.tool_output.suggestion.suggested_tool
                    for tool in tools
                ]
            ):
                parts.append(
                    Part.from_function_response(
                        message.body.tool_output.suggestion.suggested_tool,
                        message.body.tool_output.output,
                    )
                )
        return parts

    def _parse_response(
        self, response: GenerationResponse | Iterable[GenerationResponse]
    ) -> MessageBody:
        if isinstance(response, GenerationResponse):
            candidate = response.candidates[0]
            if (
                candidate.finish_reason
                == google.cloud.aiplatform_v1beta1.types.Candidate.FinishReason.STOP
            ):
                return self._parse_content(response.candidates[0].content)
            else:
                logger.warning(
                    "Gemini response did not finish with a valid reason: %s, message: %s",
                    candidate.finish_reason,
                    candidate.finish_message,
                )

                return MessageBody(
                    text="I'm sorry, I cannot generate a response: {}".format(
                        candidate.finish_message
                    )
                )

    def _parse_content(self, content: Content) -> MessageBody:
        body = MessageBody()

        if len(content.parts) == 0:
            return body

        part = content.parts[0]
        if not part:
            return body

        try:
            body.text = part.text
        except Exception:
            pass

        # body.images = [
        #     Image(uri=part.uri, base64_data=part.data, content_type=part.content_type)
        #     for part in content.parts
        #     if part.uri or part.data
        # ]

        if part.function_call:
            body.tool_suggestion = ToolSuggestion(
                suggested_tool=part.function_call.name,
                input=part.function_call.args,
            )

        return body

    def _prepare_functions(self, tools: List[ToolDefinition]):
        return [
            FunctionDeclaration(
                name=tool.name, parameters=tool.schema, description=tool.description
            )
            for tool in tools
        ]

    # def _merge_by_role(self, gemini_contents: List[Content]) -> List[Content]:
    #     merged_contents = []
    #     for content in gemini_contents:
    #         if len(merged_contents) == 0 or content.role != merged_contents[-1].role:
    #             merged_contents.append(content)
    #         else:
    #             merged_contents[-1].parts.extend(content.parts)
    #
    #     return merged_contents


class GeminiChat(Chat):
    model: GeminiModel
    chat_session: ChatSession

    def __init__(self, model: GeminiModel, chat_session: ChatSession):
        self.model = model
        self.chat_session = chat_session

    def send_message(
        self, content: List[Message], tools: List[ToolDefinition] = None, **kwargs
    ) -> MessageBody:
        gemini_content = self.model._prepare_parts(content)
        # gemini_content = self.model._merge_by_role(gemini_content)

        gemini_functions = None
        if tools:
            gemini_functions = self.model._prepare_functions(tools)

        gemini_tools = None
        if gemini_functions:
            gemini_tools = [
                Tool(
                    function_declarations=gemini_functions,
                )
            ]
        if gemini_functions:
            gemini_tools = [
                Tool(
                    function_declarations=gemini_functions,
                )
            ]

        logger.debug(f"Request to gemini chat: {gemini_content}, tools: {gemini_tools}")

        response = self.chat_session.send_message(
            gemini_content,
            tools=gemini_tools,
            generation_config=GenerationConfig(**self.model.model_kwargs, **kwargs),
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            },
        )

        message_body = self.model._parse_response(response)
        logger.debug(f"Response from gemini chat: {message_body}")

        return message_body
