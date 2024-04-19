from pydantic import BaseModel
from typing import Optional

class OaiCompletionAPIErrorMessage(BaseModel):
    message: Optional[str]
    type: Optional[str]
    param: Optional[str]
    code: str

class OaiCompletionAPIContentFilterError(Exception):
    def __init__(self, e):
        assert e.code == 'content_filter'
        self.errors = OaiCompletionAPIErrorMessage(
            message=e.message,
            type=e.type,
            param=e.param,
            code=e.code
        )

class OaiCompletionAPIContextLengthExceededError(Exception):
    def __init__(self, e):
        assert e.code == 'context_length_exceeded'
        self.errors = OaiCompletionAPIErrorMessage(
            message=e.message,
            type=e.type,
            param=e.param,
            code=e.code
        )

class OaiCompletionAPINonStopFinishReasonError(Exception):
    def __init__(self, finish_reason):
        self.errors = OaiCompletionAPIErrorMessage(
            message=finish_reason,
            type=finish_reason,
            param=finish_reason,
            code=finish_reason
        )

class OaiCompletionAPIOtherError(Exception):
    def __init__(self, e):
        self.errors = OaiCompletionAPIErrorMessage(
            message=e.message,
            type=e.type,
            param=e.param,
            code=e.code
        )

def raise_oai_error(e):
    print("raise_oai_error e", e)
    print(type(e))
    if e.code == 'content_filter': raise OaiCompletionAPIContentFilterError(e)
    elif e.code == 'context_length_exceeded': raise OaiCompletionAPIContextLengthExceededError(e)
    else: raise OaiCompletionAPIOtherError(e)