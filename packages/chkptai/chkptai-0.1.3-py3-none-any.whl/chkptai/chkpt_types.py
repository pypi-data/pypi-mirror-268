from typing import List, Optional, Union

from openai import BaseModel
from openai.types import CompletionUsage
from openai.types.chat.chat_completion import Choice as CompletionChoice
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice
from typing_extensions import Literal, Required, TypedDict


class FeedbackResponse(BaseModel):
    success: bool
    message: Optional[str] = None


class ChkptChatCompletion(BaseModel):
    chkpt_id: str
    """A unique identifier for the checkpoint-ai feedback collection."""

    id: str
    """A unique identifier for the chat completion."""

    choices: List[CompletionChoice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, which is always `chat.completion`."""

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[CompletionUsage] = None
    """Usage statistics for the completion request."""


class ChkptChatCompletionChunk(BaseModel):
    # chkpt_id: str
    """A unique identifier for the checkpoint-ai feedback collection."""

    id: str
    """A unique identifier for the chat completion. Each chunk has the same ID."""

    choices: List[ChunkChoice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created.

    Each chunk has the same timestamp.
    """

    model: str
    """The model to generate the completion."""

    object: Literal["chat.completion.chunk"]
    """The object type, which is always `chat.completion.chunk`."""

    system_fingerprint: Optional[str] = None
    """
    This fingerprint represents the backend configuration that the model runs with.
    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """


class Image(BaseModel):
    b64_json: Optional[str] = None
    """
    The base64-encoded JSON of the generated image, if `response_format` is
    `b64_json`.
    """

    revised_prompt: Optional[str] = None
    """
    The prompt that was used to generate the image, if there was any revision to the
    prompt.
    """

    url: Optional[str] = None
    """The URL of the generated image, if `response_format` is `url` (default)."""


class ImageGenerateParams(TypedDict, total=False):
    prompt: Required[str]
    """A text description of the desired image(s).

    The maximum length is 1000 characters for `dall-e-2` and 4000 characters for
    `dall-e-3`.
    """

    model: Union[str, Literal["dall-e-2", "dall-e-3"], None]
    """The model to use for image generation."""

    n: Optional[int]
    """The number of images to generate.

    Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.
    """

    quality: Literal["standard", "hd"]
    """The quality of the image that will be generated.

    `hd` creates images with finer details and greater consistency across the image.
    This param is only supported for `dall-e-3`.
    """

    response_format: Optional[Literal["url", "b64_json"]]
    """The format in which the generated images are returned.

    Must be one of `url` or `b64_json`.
    """

    size: Optional[Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]]
    """The size of the generated images.

    Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one
    of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.
    """

    style: Optional[Literal["vivid", "natural"]]
    """The style of the generated images.

    Must be one of `vivid` or `natural`. Vivid causes the model to lean towards
    generating hyper-real and dramatic images. Natural causes the model to produce
    more natural, less hyper-real looking images. This param is only supported for
    `dall-e-3`.
    """

    user: str
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse.
    [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
    """


class ChkptImagesResponse(BaseModel):
    chkpt_id: str
    created: int

    data: List[Image]
