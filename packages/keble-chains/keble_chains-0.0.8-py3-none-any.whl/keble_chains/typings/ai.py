import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, Type, Any, Dict, Iterator

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from pydantic import BaseModel

from ..utils import get_string_tokens


class AiMessageRole(str, Enum):
    system = 'system'
    user = 'user'
    assistant = 'assistant'


class AiMessageObject(ABC):

    @abstractmethod
    def to_dict(self) -> dict: ...

    @property
    @abstractmethod
    def tokens(self) -> int: ...

    @property
    @abstractmethod
    def content(self) -> str: ...

    @property
    @abstractmethod
    def role(self) -> AiMessageRole: ...


class AiPrompt(BaseModel):
    content: str
    role: AiMessageRole

    def to_dict(self) -> dict:
        return self.model_dump()

    @property
    def tokens(self) -> int:
        return AiModel.string_tokens(self.model_dump_json())

    @classmethod
    def to_oai_dicts(cls, prompts: List["AiPrompt"]) -> List[dict]:
        return [prompt.to_dict() for prompt in prompts]

    @staticmethod
    def replace_assistant_messages_in_prompts(prompts: List["AiPrompt"], replacements: List[str]) -> List["AiPrompt"]:
        """Replace ALL assistant message in a list of prompts"""
        for prompt in prompts:
            if prompt.role == AiMessageRole.assistant:
                assert len(replacements) > 0, f"Insufficient assistant message for replacement in the prompts list"
                replacement = replacements.pop(0)
                prompt.content = replacement
        return prompts

    @staticmethod
    def replace_system_message_in_prompts(prompts: List["AiPrompt"], replacement: str) -> List["AiPrompt"]:
        """Replace FIRST system message in a list of prompts"""
        assert len(prompts) > 0 and prompts[
            0].role == AiMessageRole.system, "Incorrect prompt format, expected system message as the first AiPrompt"
        prompts[0].content = replacement
        return prompts

    @staticmethod
    def replace_user_messages_in_prompts(prompts: List["AiPrompt"], replacements: List[str]) -> List["AiPrompt"]:
        """Replace ALL user message in a list of prompts"""
        for prompt in prompts:
            if prompt.role == AiMessageRole.user:
                assert len(replacements) > 0, f"Insufficient user message for replacement in the prompts list"
                replacement = replacements.pop(0)
                prompt.content = replacement
        return prompts

    def to_langchain_message(self) -> HumanMessage | SystemMessage | AIMessage:
        if self.role == AiMessageRole.assistant:
            return AIMessage(self.content)
        elif self.role == AiMessageRole.user:
            return HumanMessage(self.content)
        elif self.role == AiMessageRole.system:
            return SystemMessage(self.content)
        else:
            raise ValueError(f"Unhandled role type: {self.role}")

    @classmethod
    def from_langchain_message(cls, message: HumanMessage | SystemMessage | AIMessage) -> "AiPrompt":
        if message.type == "human":
            return cls(
                role=AiMessageRole.user,
                content=message.content
            )
        elif message.type == "system":
            return cls(
                role=AiMessageRole.system,
                content=message.content
            )
        elif message.type == "ai":
            return cls(
                role=AiMessageRole.assistant,
                content=message.content
            )
        else:
            raise ValueError(f"Unhandled message type: {message.type}")


AiMessage = AiPrompt | Tuple[str, str] | AiMessageObject | str

Vector = List[float]


def is_ai_prompt(maybe_prompt: Any) -> bool:
    return "role" in maybe_prompt and "content" in maybe_prompt and maybe_prompt["role"] in list(AiMessageRole)


def is_ai_message(maybe_message: Any) -> bool:
    if isinstance(maybe_message, dict):
        return is_ai_prompt(maybe_message)
    elif isinstance(maybe_message, tuple):
        return len(maybe_message) == 2 and maybe_message[0] in list(AiMessageRole)
    elif isinstance(maybe_message, str):
        return True
    elif isinstance(maybe_message, object):
        return hasattr(maybe_message, 'to_dict')
    return False


class AiPromptHandler(ABC):

    @abstractmethod
    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]: ...


class AiModel(AiPromptHandler):

    @abstractmethod
    def embed_texts(self, texts: str | List[str]) -> Vector | List[Vector]:
        ...

    @property
    @abstractmethod
    def tpm(self) -> int:
        ...

    @property
    @abstractmethod
    def max_token(self) -> int:
        ...

    @property
    @abstractmethod
    def deployment(self) -> str:
        ...

    @property
    @abstractmethod
    def api_version(self) -> str:
        ...

    @property
    @abstractmethod
    def endpoint(self) -> str:
        ...

    @classmethod
    def to_prompts(cls, messages: List[AiMessage]) -> List[AiPrompt]:
        tuple_reformat_ = lambda msg: AiPrompt(role=msg[0], content=msg[1])
        dict_reformat_ = lambda dict_: AiPrompt(role=dict_["role"], content=dict_["content"])
        str_reformat_ = lambda str_: AiPrompt(role=AiMessageRole.user, content=str_)
        object_reformat = lambda obj: AiPrompt(role=obj.role, content=obj.content)
        prompts = []
        for msg in messages:
            if isinstance(msg, AiPrompt):
                prompts.append(msg)
            elif isinstance(msg, tuple):
                prompts.append(tuple_reformat_(msg))
            elif isinstance(msg, dict):
                prompts.append(dict_reformat_(msg))
            elif isinstance(msg, str):
                prompts.append(str_reformat_(msg))
            elif isinstance(msg, object):

                prompts.append(object_reformat(msg))
        return prompts

    @classmethod
    def prompts_strings(cls, prompts: List[AiPrompt], *, separator: str = "\n") -> Tuple[str, str, str]:
        """Convert prompts to string for system, user and assistant"""
        system: List[str] = []
        user: List[str] = []
        assistant: List[str] = []
        for prompt in prompts:
            content = cls.message_content(prompt)
            role = cls.message_role(prompt)
            if role == AiMessageRole.assistant:
                assistant.append(content)
            elif role == AiMessageRole.system:
                system.append(content)
            elif role == AiMessageRole.user:
                user.append(content)
            else:
                raise AssertionError(f"Invalid role: {role}")
        return separator.join(system), separator.join(user), separator.join(assistant)

    @classmethod
    def messages_tokens(cls, messages: List[AiMessage] | AiMessage) -> int:
        msgs_ = messages if isinstance(messages, list) else [messages]
        tokens = 0
        for msg_ in msgs_:
            token_ = None
            if isinstance(msg_, str):
                token_ = cls.string_tokens(msg_)
            elif isinstance(msg_, tuple):
                token_ = cls.tuple_tokens(msg_)
            elif isinstance(msg_, dict):
                token_ = cls.dict_tokens(msg_)
            elif isinstance(msg_, object):
                token_ = cls.object_tokens(msg_)
            assert token_ is not None, f"Invalid type of message: {type(msg_)}"
            tokens += token_
        return tokens

    @staticmethod
    def string_tokens(string: str, encoding_name: str = "cl100k_base") -> int:
        """Return numbers of token"""
        return get_string_tokens(string=string, encoding_name=encoding_name)

    @classmethod
    def tuple_tokens(cls, tuple_: Tuple[str, str]) -> int:
        """Return numbers of token"""
        return cls.dict_tokens({"role": tuple_[0], "content": tuple_[1]})

    @classmethod
    def dict_tokens(cls, dict_: Dict[str, str]) -> int:
        """Return numbers of token"""
        msgs_ = json.dumps({"role": dict_["role"], "content": dict_["content"]})
        return cls.string_tokens(msgs_)

    @classmethod
    def object_tokens(cls, object_: AiMessageObject) -> int:
        """Return numbers of token"""
        assert hasattr(object_, "tokens")
        return object_.tokens

    @classmethod
    def message_content(cls, msg: AiMessage) -> str:
        if isinstance(msg, AiPrompt):
            return msg.content
        elif isinstance(msg, str):
            return msg
        elif isinstance(msg, tuple):
            return msg[1]
        elif isinstance(msg, dict):
            return msg["content"]
        elif hasattr(msg, "content"):
            assert isinstance(msg.content, str)
            return msg.content
        raise AssertionError(f"Invalid msg type: {type(msg)}")

    @classmethod
    def message_role(cls, msg: AiMessage) -> AiMessageRole:
        if isinstance(msg, AiPrompt):
            return msg.role
        elif isinstance(msg, str):
            return AiMessageRole.user
        elif isinstance(msg, tuple):
            return msg[0]
        elif isinstance(msg, dict):
            return msg["role"]
        elif hasattr(msg, "role"):
            assert msg.role in list(AiMessageRole)
            return msg.role
        raise AssertionError(f"Invalid msg type: {type(msg)}")

    @classmethod
    def get_latest_assistant_prompt(cls, prompts: List[AiPrompt]) -> AiPrompt:
        assert len(prompts) > 0, "Empty prompts"
        last_prompt = prompts[-1]
        assert last_prompt.role == AiMessageRole.assistant, "Last prompt's role is not assistant"
        return last_prompt

    @abstractmethod
    def stream(self, prompts: List[AiPrompt]) -> Iterator[List[AiPrompt]]:
        ...


class AiModelTokenManager(ABC):

    @abstractmethod
    def wait_for_allow(self, require_token: int, *, ai_model: Type[AiModel]): ...


class AiSession(AiPromptHandler, ABC):

    def continue_process(self, new_prompts: List[AiPrompt]) -> List[AiPrompt]:
        return self.process(self.prompts + new_prompts)

    def process_messages(self, messages: List[AiMessage]) -> List[AiPrompt]:
        return self.process(AiModel.to_prompts(messages))

    def continue_process_messages(self, new_messages: List[AiMessage]) -> List[AiPrompt]:
        return self.process(self.prompts + AiModel.to_prompts(new_messages))

    @property
    @abstractmethod
    def ai_model(self) -> AiModel: ...

    @property
    @abstractmethod
    def prompts(self) -> List[AiPrompt]:
        """Get its entire prompt in this session"""

    @prompts.setter
    @abstractmethod
    def prompts(self, messages: List[AiMessage]):
        """Set its entire prompt in this session"""
