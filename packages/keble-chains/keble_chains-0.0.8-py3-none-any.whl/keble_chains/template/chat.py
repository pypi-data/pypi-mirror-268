from abc import ABC, abstractmethod
from typing import Optional, List
from ..typings import AiMessageRole, AiPrompt, AiModel
from ..utils import cut_content_by_token, get_string_tokens
import json
from partialjson.json_parser import JSONParser




class SectionContentABC(ABC):
    @property
    @abstractmethod
    def str(self) -> str: ...


class StringTemplate:

    def __init__(self, *, max_tokens: Optional[int] = None):
        self.__max_tokens = max_tokens

    @classmethod
    def limit_tokens(cls, content: str, max_tokens: Optional[int]):
        if max_tokens is None: return content
        require_tokens = get_string_tokens(content)
        if require_tokens > max_tokens:
            return cut_content_by_token(content, token_available=max_tokens)
        return content

    def _limit_tokens(self, content: str):
        return self.limit_tokens(content, max_tokens=self.__max_tokens)


SectionContent = SectionContentABC | str | dict | tuple | List[str]


class SubjectTemplate(StringTemplate):
    def __init__(self, *, subject: str, sections_template: Optional["SectionsTemplate"] = None,
                 hints_template: Optional["HintsTemplate"] = None, json_template: Optional["JsonTemplate"] = None,
                 **kwargs):
        super(SubjectTemplate, self).__init__(**kwargs)
        self.__sections_template = sections_template
        self.__hints_template = hints_template
        self.__json_template = json_template
        self.__subject = subject

    def subject(self):
        hints = f"\n{self.__hints_template.hints()}" if self.__hints_template is not None else ""
        sections_definitions = f"\n{self.__sections_template.subject()}" if self.__sections_template is not None else ""
        json_definitions = f"\n{self.__json_template.subject()}" if self.__json_template is not None else ""
        json_response_prefix = "Your response format must be a JSON.\n" if self.__json_template is not None else ""
        return self._limit_tokens(
            content=f"{self.__subject}{json_response_prefix}{sections_definitions}{json_definitions}{hints}")

    def prompt(self) -> AiPrompt:
        return AiPrompt(role=AiMessageRole.system, content=self.subject())


class MessageTemplate:
    def __init__(self, *, sections_template: "SectionsTemplate"):
        self.__sections_template = sections_template

    def content(self, contents: List[SectionContent]) -> str:
        return self.__sections_template.contents(contents=contents)

    def prompt(self, contents: List[SectionContent], role: AiMessageRole = AiMessageRole.user) -> AiPrompt:
        return AiPrompt(role=role, content=self.content(contents))


class JsonTemplate:

    def __init__(self, templates: List["JsonKeyTemplate"]):
        self.__templates = templates

    def subject(self):
        # definitions = [template.definition() for template in self.__templates]
        definitions_strings: List[str] = [f'There are {len(self.__templates)} fields of the json you need to fill:']
        for index, template in enumerate(self.__templates):
            definitions_strings.append(template.definition(index=index))
        definitions_strings.append("\nIf a key you can not determine, you should mark it as null.\n")
        return "\n".join(definitions_strings)

    @classmethod
    def parse_incomplete_json(cls, incomplete_json: str):
        """Get Key-Value from a partially streaming JSON"""
        json_parser = JSONParser()
        return json_parser.parse(incomplete_json)



class SectionsTemplate:

    def __init__(self, *, templates: List["SectionTemplate"], empty_placeholder: str = "<empty>"):
        self.__templates = templates
        self.__empty_placeholder = empty_placeholder

    def contents(self, contents: List[SectionContent]):
        assert len(self.__templates) == len(
            contents), f"Incompatible contents and templates. They have different length"
        contents_strings: List[str] = []
        for index, content in enumerate(contents):
            template = self.__templates[index]
            contents_strings.append(
                template.content(content=content, index=index, empty_placeholder=self.__empty_placeholder))
        return "\n\n\n".join(contents_strings)

    def subject(self):
        sections_names = ", ".join([f'"{template.name}"' for template in self.__templates])
        definitions_strings: List[str] = [
            f'You will be provided by {len(self.__templates)} sections of information: {sections_names}. All these information are given by user and intended to help you to create an better response.']
        for index, template in enumerate(self.__templates):
            definitions_strings.append(template.definition(index=index))
        definitions_strings.append("\nIf a section is empty, it will be marked as <empty>.\n")
        return "\n".join(definitions_strings)


class HintsTemplate:
    def __init__(self, *, templates: List["HintTemplate"]):
        self.__templates = templates

    def hints(self):
        definitions_strings: List[str] = ["\n\nHere are some hints to help you:"]

        for index, template in enumerate(self.__templates):
            definitions_strings.append(
                template.definition(index=index))
        return "\n".join(definitions_strings)


class JsonKeyTemplate(StringTemplate):

    def __init__(self, *, definition: str, key: str, **kwargs):
        super().__init__(**kwargs)

        self.__key = key
        self.__definition = definition

    def definition(self, *, index: Optional[int] = None) -> str:
        if index is not None:
            c = f"Key {index + 1}{self.__key}: {self.__definition}"
        else:
            c = f"Key {self.__key}: {self.__definition}"
        return self._limit_tokens(c)


class SectionTemplate(StringTemplate):

    def __init__(self, *, definition: str, name: Optional[str] = None, section_prefix: str = "Section", **kwargs):
        super(SectionTemplate, self).__init__(**kwargs)
        self.__name = name
        self.__definition = definition
        assert self.__name is None or len(self.__name) <= 50, f"Name is too long for a Section Template: {self.__name}"
        assert self.__definition is not None and len(
            self.__definition) <= 1000, f"Definition is too long for a Section Template: {self.__definition}"
        self.__section_prefix = section_prefix

    @property
    def name(self) -> str:
        return self.__name

    def content(self, *, content: Optional[SectionContent] = None, index: Optional[int] = None,
                empty_placeholder: Optional[str] = "<empty>") -> str:
        if index is not None:
            c = f"{self.__section_prefix} {index + 1}{self.__name_string()}: {self.__content_string(content, empty_placeholder=empty_placeholder)}"
        else:
            c = f"{self.__section_prefix}{self.__name_string()}: {self.__content_string(content, empty_placeholder=empty_placeholder)}"
        return self._limit_tokens(c)

    def definition(self, *, index: Optional[int] = None) -> str:
        if index is not None:
            return f"{self.__section_prefix} {index + 1}{self.__name_string()}: {self.__definition}"
        else:
            return f"{self.__section_prefix}{self.__name_string()}: {self.__definition}"

    def __content_string(self, content: SectionContent, *, empty_placeholder: str) -> str:
        if not content: return empty_placeholder
        if isinstance(content, str): return content
        if isinstance(content, dict): return "; ".join([f"{key}: {val}" for key, val in content.items()])
        if isinstance(content, tuple) or isinstance(content, list): return ", ".join(content)
        assert hasattr(content, "str"), "Missing str property for content"
        return content.str

    def __name_string(self):
        if self.__name: return f" \"{self.__name}\""  # with space
        return ""


class HintTemplate(SectionTemplate):

    def __init__(self, hint: str):
        super(HintTemplate, self).__init__(definition=hint, section_prefix="Hint")

    def content(self, *args, **kwargs) -> str:
        raise AssertionError("no content for hint, only definition")
