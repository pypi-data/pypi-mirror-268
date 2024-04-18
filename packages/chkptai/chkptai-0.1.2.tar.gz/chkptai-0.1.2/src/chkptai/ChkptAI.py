from openai import OpenAI, Stream
from openai._base_client import Body, Headers, Query, make_request_options
from openai._client import NOT_GIVEN, NotGiven

import httpx

from chkptai.chkpt_types import (
    ChkptChatCompletion,
    ChkptImagesResponse,
    ChkptChatCompletionChunk,
    FeedbackResponse
)


class OpenAIProxy(OpenAI):
    """
    A proxy class for OpenAI's API client that intercepts method calls to potentially
    modify their execution and responses. This proxy allows for custom processing
    of responses, especially for methods related to chat completions and image generation.

    Attributes:
        _client (OpenAI): The original OpenAI client instance being proxied.
    """
    def __init__(self, client):
        """
        Initializes a new instance of the OpenAIProxy class.

        Args:
            client (OpenAI): The original OpenAI client to be proxied.
        """
        self._client = client

    def __getattr__(self, name):
        """
        Intercept attribute access to wrap callable attributes with custom logic or
        to return a proxy for non-callable attributes, enabling deep interception.

        Args:
            name (str): The attribute name that is being accessed.

        Returns:
            Any: A wrapped callable or another proxy instance for nested attributes.
        """
        attr = getattr(self._client, name)

        # Return a new proxy if the attribute accessed is not callable,
        # this handles nested attributes like `chat.completions.create`
        if callable(attr):
            return self._wrap_call(attr)
        else:
            return OpenAIProxy(attr)  # Return a proxy for nested non-callable attributes

    def _wrap_call(self, func):
        """
        Wraps a callable attribute to modify its behavior or its return values.

        Args:
            func (callable): The original function from the OpenAI client to wrap.

        Returns:
            callable: A wrapped function that includes custom processing logic.
        """
        def wrapped(*args, **kwargs):
            # Execute the original function
            result = func(*args, **kwargs)
            # Modify the result if it's the chat completions create method
            if isinstance(result, Stream) and 'Completions' in func.__qualname__ and func.__name__ == 'create':
                return self._wrap_stream(result)
            if 'Completions' in func.__qualname__ and func.__name__ == 'create':
                return ChkptChatCompletion.model_validate(result.model_dump())
            elif 'Images' in func.__qualname__ and func.__name__ == 'generate':
                return ChkptImagesResponse.model_validate(result.model_dump())
            else:
                return result
        return wrapped

    def _wrap_stream(self, stream):
        """
        Wraps a streaming response to modify data items as they are yielded.

        Args:
            stream (Stream): The original stream object from the OpenAI client.

        Returns:
            Generator: A generator that yields modified data items.
        """
        def generator():
            for item in stream:
                modified_item = ChkptChatCompletionChunk.model_validate(item.model_dump())
                yield modified_item

        return generator()

class ChkptAI:
    """
    A class that provides high-level functionality for interacting with the OpenAI API
    through a proxied client. It includes methods for sending feedback directly to
    Checkpoint-AI services for model alignment.

    Attributes:
        _base_url (str): The base URL for the API endpoints.
        _raw_client (OpenAI): A direct, non-proxied OpenAI client for certain operations.
        client (OpenAIProxy): The proxied OpenAI client that applies custom processing.
    """
    _base_url = "https://api.checkpoint-ai.com/v1"

    def __init__(self, api_key: str):
        self._raw_client = OpenAI(api_key=api_key, base_url=self._base_url)
        self.client = OpenAIProxy(self._raw_client) 
    
    def send_feedback(
        self,
        response: str | ChkptChatCompletion | ChkptChatCompletionChunk,
        name: str,
        value: float,
        index: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        """
        Sends feedback directly using the non-proxied raw client. This method bypasses
        the proxy to ensure feedback is sent without interception.

        Args:
            response (str | ChkptChatCompletion | ChkptChatCompletionChunk): The response ID or
                the response object to which feedback is being sent.
            name (str): The name of the feedback parameter.
            value (float): The value of the feedback.
            index (int): The index of the message within the response to which the feedback relates.
            extra_headers (Headers | None): Additional headers to be sent with the request.
            extra_query (Query | None): Additional query parameters to be sent with the request.
            extra_body (Body | None): Additional body data to be sent with the request.
            timeout (float | httpx.Timeout | None | NotGiven): The timeout configuration for the request.

        Returns:
            FeedbackResponse: The response from the feedback submission endpoint.
        """
        if isinstance(response, (ChkptChatCompletion | ChkptChatCompletionChunk)):
            response_id = response.chkpt_id
        else:
            response_id = response
        return self._raw_client.post(
            "/feedback/send",
            body={
                "feedback": [{"name": name, "value": value, "index": index}],
                "id": response_id,
            },
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=FeedbackResponse,
            stream=False,
        )
    
