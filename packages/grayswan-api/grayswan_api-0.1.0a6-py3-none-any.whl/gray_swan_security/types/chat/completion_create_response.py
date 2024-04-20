# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CompletionCreateResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "Usage",
]


class ChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class ChoiceMessageToolCall(BaseModel):
    id: str

    function: ChoiceMessageToolCallFunction

    type: Literal["function"]


class ChoiceMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]

    index: int

    message: ChoiceMessage

    logprobs: Union[str, object, None] = None


class Usage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int


class CompletionCreateResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: Literal["chat.completion"]

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
