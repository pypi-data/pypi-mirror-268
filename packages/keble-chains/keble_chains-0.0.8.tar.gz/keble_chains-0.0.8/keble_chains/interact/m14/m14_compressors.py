from typing import List, Callable, Tuple, Optional
from ...typings.ai import AiPromptHandler, AiPrompt, AiModel, is_ai_prompt, AiSession, AiMessageRole
from ...utils.main import split_string_into_slices


class M14Compress(AiPromptHandler):
    def __init__(self, *, msg_handler: Callable[[AiPrompt, int], Tuple[AiPrompt, int, bool] | AiPrompt]):
        self.__msg_handler = msg_handler

    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        parsed: List[AiPrompt] = []
        cumulative_tokens = 0
        for prompt in prompts:
            res, tokens, break_ = self.__parse_processed_res(self.__msg_handler(prompt, cumulative_tokens))
            if res is not None: parsed.append(res)
            if break_: break
        return parsed

    def __parse_processed_res(self, res: Tuple[AiPrompt, int, bool] | AiPrompt) -> Tuple[Optional[AiPrompt], int, bool]:
        """Return parsed result, and bool indicating should it stop or continue
        bool: true for break, false for continue
        """
        if res is None: return None, 0, True
        is_prompt = is_ai_prompt(res)
        if is_prompt: return res, AiModel.messages_tokens(res), False
        assert isinstance(res, tuple), f"Invalid format of compress response: {res}"
        return res

    @staticmethod
    def cut_content_by_token(content: str, token_available: int):
        slice_size = 10
        split_: List[str] = split_string_into_slices(content, slice_size)
        last_string = ""
        for sp in split_:
            new_token = AiModel.string_tokens(last_string + sp)
            if new_token < token_available:
                last_string += sp
            else:
                break
        return last_string


class M14CompressByLength(M14Compress):

    def __init__(self, *, max_token: int = 500):
        super().__init__(msg_handler=self._process)
        self.__max_token = max_token

    def _process(self, msg: AiPrompt, used_tokens: int) -> Tuple[Optional[AiPrompt], int, bool]:
        """Return Tuple[Message, Require Tokens, Break/Stop]"""
        require_tokens = AiModel.messages_tokens([msg])
        if used_tokens + require_tokens < self.__max_token:
            return msg, require_tokens, False
        else:
            # exceed
            role = AiModel.message_role(msg)
            trimmed = self.cut_content_by_token(AiModel.message_content(msg), self.__max_token - used_tokens)
            if trimmed is not None and len(trimmed) > 0:
                prompt: AiPrompt = AiPrompt(role=role, content=trimmed)
                return prompt, AiModel.messages_tokens([prompt]), False
            return None, 0, True


class M14CompressBySummary(AiPromptHandler):

    def __init__(self, *, session: AiSession,
                 get_summary_messages: Callable[[List[AiPrompt], Optional[List[AiPrompt]]], List[AiPrompt]] = None,
                 parse_summary_message: Callable[[List[AiPrompt], List[AiPrompt]], Tuple[List[AiPrompt], bool]]):
        self.__session = session
        self.__get_summary_messages = get_summary_messages if get_summary_messages is not None else self.default_get_summary_messages
        self.__parse_summary_message = parse_summary_message if parse_summary_message is not None else self.default_parse_summary_message

    def process(self, prompts: List[AiPrompt]) -> List[AiPrompt]:
        """M14Compress messages by summary"""
        previous_summaries: Optional[List[AiPrompt]] = None
        break_ = False
        tried = 0
        max_tried = 5
        while not break_ and tried < max_tried:
            tried += 1
            messages_: List[AiPrompt] = self.__get_summary_messages(prompts, previous_summaries)
            ai_prompts: List[AiPrompt] = self.__session.process(messages_)
            previous_summaries, break_ = self.__parse_summary_message(prompts, ai_prompts)
            if tried >= max_tried:
                raise AssertionError(f"Failed to compress summary in {tried} attempts")

        # return a compressed version of the List[AiMessage]
        return previous_summaries

    @classmethod
    def default_get_summary_messages(cls, prompts: List[AiPrompt],
                                     previous_summaries: Optional[List[AiPrompt]] = None) -> List[AiPrompt]:
        system_messages: List[AiPrompt] = [AiPrompt(role=AiMessageRole.system, content="You are a summarize assistant. You help me to summarize any given messages. You will try to remove duplicate information. Your summarize should be prefix with \"Summary:\". If user reply \"shorter\". You need to make your summary shorter.")]
        if previous_summaries is not None and len(previous_summaries) > 0:
            # try to make previous summary shorter
            return system_messages + prompts + previous_summaries + [AiPrompt(role=AiMessageRole.user, content="shorter")]
        # try to make entire messages shorter
        return system_messages + prompts

    @classmethod
    def default_parse_summary_message(cls, original_prompts: List[AiPrompt], all_prompts: List[AiPrompt]) -> Tuple[
        List[AiPrompt], bool]:
        """Return list of summary, should it stop/break"""
        summaries: List[str] = []
        prompts: List[AiPrompt] = []
        prefix = "Summary:"
        for prompt in reversed(all_prompts):
            role = AiModel.message_role(prompt)
            content = AiModel.message_content(prompt)
            if role == AiMessageRole.user:
                return prompts, True
            elif prefix in content and content.index(prefix) == 0:
                content_ = content[len(prefix):]
                prompts.insert(0, prompt)
                summaries.insert(0, content_)
        return prompts, True


