import tiktoken
from typing import List

def split_string_into_slices(s, slice_size):
    return [s[i:i + slice_size] for i in range(0, len(s), slice_size)]


def get_string_tokens(string: str, encoding_name: str = "cl100k_base") -> int:
    """Return numbers of token"""
    # https://stackoverflow.com/questions/75804599/openai-api-how-do-i-count-tokens-before-i-send-an-api-request
    # https://github.com/openai/tiktoken
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def cut_content_by_token(content: str, token_available: int):
    slice_size = 10
    split_: List[str] = split_string_into_slices(content, slice_size)
    last_string = ""
    for sp in split_:
        new_token = get_string_tokens(last_string + sp)
        if new_token < token_available:
            last_string += sp
        else:
            break
    return last_string