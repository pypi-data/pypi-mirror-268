# tests/test_main.py

from unittest.mock import patch, MagicMock
import pytest
import sys
from vectara_cli.main import main

# Test the successful execution of a valid command
@patch('vectara_cli.main.get_vectara_client')
@patch('vectara_cli.commands.index_document.main')
def test_valid_command_execution(mock_index_document_main, mock_get_vectara_client):
    vectara_client_mock = MagicMock()
    mock_get_vectara_client.return_value = vectara_client_mock

    with patch.object(sys, 'argv', ['main.py', 'index-document', 'dummy_arg']):
        main()

    mock_index_document_main.assert_called_once_with(['dummy_arg'], vectara_client_mock)

# Test handling of 'set-api-keys' with incorrect number of arguments and verifying printed error
def test_set_api_keys_incorrect_args():
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ['main.py', 'set-api-keys', 'only_one_arg']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1
            mock_print.assert_called_with("Error: set-api-keys requires exactly 2 arguments: customer_id and api_key.")

# Test unknown command STDERR handling and verifying correct error print
def test_unknown_command_stderr():
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ['main.py', 'nonexistent-command']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1
            mock_print.assert_called_with("vectara: 'nonexistent-command' is not a vectara command. See 'vectara --help'.")
