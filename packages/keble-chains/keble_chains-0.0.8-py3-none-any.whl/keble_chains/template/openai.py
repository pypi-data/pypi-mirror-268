from abc import ABC, abstractmethod
from typing import List
from ..typings import AiMessage


class OpenaiTemplateABC(ABC):

    @property
    @abstractmethod
    def subject_message(self) -> AiMessage: ...

    @abstractmethod
    def get_non_subject_messages(self, *args, **kwargs) -> List[AiMessage]: ...

    def get_messages(self, *args, **kwargs) -> List[AiMessage]:
        return [self.subject_message] + self.get_non_subject_messages(*args, **kwargs)
