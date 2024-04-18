# tests/test_main.py
import pytest
from unittest.mock import patch
from main import main_menu, execute_transcript

@patch('builtins.print')
@patch('builtins.input', side_effect=['3'])  # Simulate user choosing to exit
def test_main_menu_exit(mock_input, mock_print):
    main_menu()
    mock_print.assert_called_with("Saliendo del programa...")

@patch('os.path.exists', return_value=True)
@patch('os.listdir', return_value=['test.txt'])
@patch('file_extractor.extract_text', return_value="Test text")
def test_execute_transcript(mock_exists, mock_listdir, mock_extract):
    assert execute_transcript('dummy/path') == "Test text"
