import pytest
from unittest.mock import patch

from chkptai import ChkptAI
from chkptai.ChkptAI import OpenAIProxy
from chkptai.chkpt_types import ChkptChatCompletion

from openai.resources.chat import Completions
from openai.resources import Images

@pytest.fixture
def chkptai():
    return ChkptAI("fake-api-key")

def test_chkptai_client_is_wrapped_by_openai_proxy(chkptai):
    assert isinstance(chkptai.client, OpenAIProxy)

def test_chat_completion_create_wrapper_by_openaiproxy(chkptai):
    # Mock the response object that func will return
    expected_validated_response = {"id": "chatcmpl-123", "content": "Processed content"}

    mock_response = {"id": "chatcmpl-123", "content": "Processed content"}

    # Patch the method that `func` in the wrapped call would actually execute
    with patch.object(OpenAIProxy, '_wrap_call', autospec=True) as mock_wrap_call:
        # Setup mock_wrap_call to execute a lambda that simulates the wrapping and just returns mock_response
        mock_wrap_call.side_effect = lambda self, func: lambda *args, **kwargs: mock_response

        # Perform the chat completion
        response = chkptai.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello what's the speed of light and what's its meaning in the universe!"}
            ]
        )
        # Validate that the response is what we expected from model_validate
        assert response == expected_validated_response, f"Expected response to be {expected_validated_response}, but got {response}"

        # Ensure that our mocked wrapped call was used
        # Assert that _wrap_call was called with the specific method
        actual_call = mock_wrap_call.call_args[0][1]  # This gets the 'func' argument from the call
        assert actual_call.__name__ == 'create', "The wrapped function should be 'create'"
        assert isinstance(actual_call.__self__, Completions), "The function should be bound to a Completions object"
        mock_wrap_call.assert_called_once()
        
def test_image_generation_model_wrapper_by_openaiproxy(chkptai):
    # Mock the response object that func will return
    mock_response = {"id": "image-123", "status": "completed"}
    expected_validated_response = {"id": "image-123", "status": "completed"}

    # Patch the method that `func` in the wrapped call would actually execute
    with patch.object(OpenAIProxy, '_wrap_call', autospec=True) as mock_wrap_call:
        # Setup mock_wrap_call to execute a lambda that simulates the wrapping and just returns mock_response
        mock_wrap_call.side_effect = lambda self, func: lambda *args, **kwargs: mock_response

        # Perform the image generation
        response = chkptai.client.images.generate(
            model="dall-e-3",
            prompt="A cute baby samoyed dog with a hat on its head.",
            n=1,
            size="1024x1024"
        )

        # Validate that the response is what we expected from model_validate
        assert response == expected_validated_response, f"Expected response to be {expected_validated_response}, but got {response}"

        # Ensure that our mocked wrapped call was used
        mock_wrap_call.assert_called_once()

        # Assert that _wrap_call was called with the specific method
        actual_call = mock_wrap_call.call_args[0][1]  # This gets the 'func' argument from the call
        assert actual_call.__name__ == 'generate', "The wrapped function should be 'generate'"
        assert isinstance(actual_call.__self__, Images), "The function should be bound to an Images object"
        
        
def test_send_feedback(mocker, chkptai):
    # Mock the response from chat completions
    mock_chat_response = ChkptChatCompletion(
        chkpt_id="chatcmpl-123",
        id="chatcmpl-123",
        choices=[],
        created=123456789,
        model="gpt-3.5-turbo",
        object="chat.completion"
    )
    
    # Mock the `create` method on the chat completions to return the mock chat response
    mocker.patch.object(chkptai.client.chat.completions, 'create', return_value=mock_chat_response)

    # Mock the HTTP post method used by the raw client to send feedback
    mock_post = mocker.patch('openai.OpenAI.post', return_value={"status": "success"})

    # Execute send_feedback
    feedback_response = chkptai.send_feedback(
        response=mock_chat_response,
        name="helpfulness",
        value=1.0,
        index=0
    )

    # Assert the HTTP post was called correctly
    mock_post.assert_called_once_with(
        "/feedback/send",
        body={
            "feedback": [{"name": "helpfulness", "value": 1.0, "index": 0}],
            "id": "chatcmpl-123",
        },
        options=mocker.ANY,
        cast_to=mocker.ANY,
        stream=False
    )
    
    # Assert the response from send_feedback
    assert feedback_response == {"status": "success"}, "Feedback response should match the mocked response"