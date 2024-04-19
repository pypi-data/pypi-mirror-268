from ...typings.ai import AiModel, AiSession, AiPrompt, AiMessage
from typing import List, Iterator


class Session(AiSession):

    def __init__(self, ai_model: AiModel):
        self.__ai_model = ai_model
        self.__prompts: List[AiPrompt] = []

    @property
    def ai_model(self): return self.__ai_model

    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        # update the current prompts (replace it)
        self.__prompts = prompts
        # complete
        returned_prompts = self.ai_model.process(self.__prompts)

        # this is wrong
        # self.__prompts += returned_prompts
        self.__prompts = returned_prompts
        return returned_prompts

    def stream(self, prompts: List[AiPrompt]) -> Iterator[List[AiPrompt]]:
        self.__prompts = prompts
        # complete
        iterator = self.ai_model.stream(self.__prompts)
        ai_prompts = None
        while True:
            try:
                next_item = next(iterator)
                yield next_item
                ai_prompts = next_item
            except StopIteration:
                break

        if ai_prompts is not None:
            self.__prompts = ai_prompts

    @property
    def prompts(self) -> List[AiPrompt]: return self.__prompts

    @prompts.setter
    def prompts(self, messages: List[AiMessage]):
        self.__prompts = AiModel.to_prompts(messages)
