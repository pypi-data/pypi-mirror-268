# tests/test_chatbot.py
import pytest
from unittest.mock import patch
from chatbot import setup_api_key, chat_with_gpt

def test_setup_api_key():
    setup_api_key('test_key')
    from chatbot import api_key
    assert api_key == 'test_key'

@patch('chatbot.openai.ChatCompletion.create')
def test_chat_with_gpt(mock_chat):
    setup_api_key('test_key')  # Setting up the API key
    mock_chat.return_value = {"choices": [{"message": {"content": "Hello, how can I help you?"}}]}
    # Adjust this test to handle user input and output interaction
