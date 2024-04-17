# ./tests/test_delete_corpus.py

import pytest
from unittest.mock import patch, MagicMock
from vectara_cli.commands.delete_corpus import main

@pytest.fixture
def mock_client_success():
    """Simulates successful deletion."""
    class MockSuccessClient:
        def delete_corpus(self, corpus_id):
            return "Deletion successful", True
    return MockSuccessClient()

@pytest.fixture
def mock_client_failure():
    """Simulates failed deletion."""
    class MockFailureClient:
        def delete_corpus(self, corpus_id):
            return "Deletion failed", False
    return MockFailureClient()

@pytest.fixture
def mock_config_manager():
    """Mocks ConfigManager to return predetermined values."""
    with patch('vectara_cli.commands.delete_corpus.ConfigManager') as mock:
        mock.get_api_keys.return_value = (123, "api_key")
        yield mock

def test_delete_corpus_without_args(capfd):
    """Tests if the deletion function behaves correctly when no arguments are passed."""
    with patch('sys.argv', ["delete_corpus"]):
        with patch('vectara_cli.commands.delete_corpus.show_delete_corpus_help') as mock_help:
            mock_help.return_value = "\nUSAGE: delete_corpus [OPTIONS] CORPUS_ID\n"
            main([], None)
            out, _ = capfd.readouterr()
            assert "USAGE" in out

def test_delete_corpus_successful(mock_client_success, mock_config_manager, capfd):
    """Tests successful deletion scenario."""
    with patch('sys.argv', ["delete_corpus", "1234"]):
        with patch('vectara_cli.commands.delete_corpus.main', return_value=mock_client_success):
            main(['1234'], mock_client_success)
            out, _ = capfd.readouterr()
            assert "Corpus deleted successfully." in out

def test_delete_corpus_failure(mock_client_failure, mock_config_manager, capfd):
    """Tests failed deletion scenario."""
    with patch('sys.argv', ["delete_corpus", "1234"]):
        with patch('vectara_cli.commands.delete_corpus.main', return_value=mock_client_failure):
            main(['1234'], mock_client_failure)
            out, _ = capfd.readouterr()
            assert "Failed to delete corpus:" in out

def test_delete_corpus_with_exception(mock_config_manager, capfd):
    """Tests the scenario where an exception is raised."""
    class MockClientException:
        def delete_corpus(self, corpus_id):
            raise ValueError("An error occurred")

    with patch('sys.argv', ["delete_corpus", "1234"]):
        with patch('vectara_cli.commands.delete_corpus.main', return_value=MockClientException()):
            main(['1234'], MockClientException())
            out, _ = capfd.readouterr()
            assert "An error occurred" in out