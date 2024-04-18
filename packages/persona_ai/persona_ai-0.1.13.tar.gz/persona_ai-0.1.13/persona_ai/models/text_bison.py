import json
from typing import Union, List

import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.language_models._language_models import (
    MultiCandidateTextGenerationResponse,
)

from persona_ai.models.base import GenAIModel
from persona_ai.domain.conversations import Message, MessageBody
from persona_ai.tools.base import ToolDefinition


class TextBisonModel(GenAIModel):
    """
    Represents a text generation model using the TextBison model.
    """

    model_name = "text-bison"
    palm: TextGenerationModel
    model_kwargs = {}

    def __init__(
        self,
        service_account: str = None,
        project_id: str = None,
        location: str = None,
        model_name: str = "text-bison",
        **kwargs,
    ):
        vertexai.init(
            service_account=service_account, project=project_id, location=location
        )
        self.model_name = model_name
        self.palm = TextGenerationModel.from_pretrained(self.model_name)
        self.model_kwargs = kwargs

    def generate(
        self,
        contents: Union[str, Message, List[Message]],
        tools: List[ToolDefinition] = None,
        **kwargs,
    ) -> MessageBody:
        palm_content = self._prepare_contents(contents)

        if tools:
            palm_content = palm_content.replace(
                "{{tools}}", self._render_tool_descriptions(tools)
            )
            palm_content = palm_content.replace(
                "{{tool_names}}", self._get_tool_names(tools)
            )

        response = self.palm.predict(palm_content, **self.model_kwargs, **kwargs)

        return self._parse_response(response)

    def _prepare_contents(self, content: Union[str, Message, List[Message]]):
        if isinstance(content, str):
            return content
        if isinstance(content, Message):
            return content.body.text
        if isinstance(content, list):
            return "\n".join([message.body.text for message in content])

    def _parse_response(
        self, response: MultiCandidateTextGenerationResponse
    ) -> MessageBody:
        return MessageBody(text=response.text)

    def _render_tool_descriptions(self, tool_definitions: List[ToolDefinition]):
        return "\n".join(
            [
                f"{tool.name}: {tool.description}, input schema: {json.dumps(tool.schema)}"
                for tool in tool_definitions
            ]
        )
        pass

    def _get_tool_names(self, tool_definitions: List[ToolDefinition]):
        return ", ".join([tool.name for tool in tool_definitions])
