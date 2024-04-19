from typing import List, Optional

from ...typings import Vector
from ...typings.ai import AiModel, AiPrompt, AiPromptHandler, AiMessageRole


class FakeAiModel(AiModel):

    def __init__(self, *, prompt_handler: Optional[AiPromptHandler] = None, static_response: Optional[AiPrompt] = None):
        assert static_response is None or static_response.role is AiMessageRole.system
        self.__prompt_handler = prompt_handler
        self.__static_response = static_response

    @property
    def tpm(self):
        return None  # it is just unlimited

    @property
    def max_token(self):
        return None

    @property
    def endpoint(self):
        return None

    @property
    def api_version(self):
        return None

    @property
    def deployment(self):
        return None

    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        if self.__static_response is not None: return self.__static_process(prompts=prompts)
        return self.__prompt_handler.process(prompts)

    def __static_process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        return prompts + [self.__static_response]

    def embed_texts(self, texts: str | List[str]) -> Vector | List[Vector]:
        raise AssertionError("FakeAiModel does not support embed_texts")
