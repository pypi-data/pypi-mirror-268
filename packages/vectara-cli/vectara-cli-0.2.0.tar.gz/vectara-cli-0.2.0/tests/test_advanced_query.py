# test_advanced_query.py

import pytest
import json
from unittest.mock import patch, MagicMock
from vectara_cli.commands.advanced_query import main as advanced_query_main


class TestAdvancedQuery:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.vectara_client_mock = MagicMock()

    @pytest.fixture
    def standard_args(self):
        return ['script.py', 'test query', '2', '123', json.dumps({}), json.dumps({})]

    def test_main_success(self, capsys, standard_args):
        self.vectara_client_mock.advanced_query.return_value = {'results': ['Result 1', 'Result 2']}
        advanced_query_main(standard_args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert 'Result 1' in captured.out
        assert 'Result 2' in captured.out

    def test_main_few_arguments(self, capsys):
        args = ['script.py', 'test query']
        advanced_query_main(args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert "Error: Not enough arguments" in captured.out

    def test_main_invalid_json(self, capsys, standard_args):
        standard_args[4] = "{invalid_json}"
        advanced_query_main(standard_args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert 'Error: Invalid JSON' in captured.out

    def test_main_num_results_not_an_integer(self, capsys, standard_args):
        standard_args[2] = 'not_a_number'
        advanced_query_main(standard_args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert 'Error: Invalid number of results' in captured.out

    def test_no_response_from_query(self, capsys, standard_args):
        self.vectara_client_mock.advanced_query.return_value = {}
        advanced_query_main(standard_args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert '{}' in captured.out

    def test_error_handling(self, capsys, standard_args):
        error_message = "Unexpected error"
        self.vectara_client_mock.advanced_query.side_effect = Exception(error_message)
        advanced_query_main(standard_args, self.vectara_client_mock)
        captured = capsys.readouterr()
        assert f"Error: {error_message}" in captured.out