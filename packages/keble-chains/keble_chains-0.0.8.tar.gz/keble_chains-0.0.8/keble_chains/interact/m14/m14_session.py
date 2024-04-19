from ..ai import Session
from typing import List
from ...typings.ai import AiModel, AiPrompt, AiPromptHandler

class M14Session(Session):
    """
    M.14 stand for Matryoshka Doll
    M.14.Message stand for Matryoshka Doll Message
    """
    def __init__(self, ai_model: AiModel, before_process: List[AiPromptHandler] = None, after_process: List[AiPromptHandler] = None):
        super().__init__(ai_model=ai_model)
        self.__before_process_handlers: List[AiPromptHandler] = before_process if before_process is not None else []
        self.__after_process_handlers: List[AiPromptHandler]  = after_process if after_process is not None else []

    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        prompts: List[AiPrompt] = super().process(self.__before_process(prompts))
        self.prompts = self.__after_process(prompts)
        return self.prompts

    def __before_process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        return self.__apply_process_handlers(prompts, self.__before_process_handlers)

    def __after_process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        return self.__apply_process_handlers(prompts, self.__after_process_handlers)

    def __apply_process_handlers(self, prompts: List[AiPrompt], handlers: List[AiPromptHandler]) -> List[AiPrompt]:
        prompts_ = prompts
        for _handler in handlers:
            prompts_ = _handler.process(prompts)
        return prompts_




