# /tests/test_create_corpus.py

import json
import pytest
from unittest.mock import patch, MagicMock

from vectara_cli.commands.create_corpus import parse_args, parse_json_arg, main
from vectara_cli.data.defaults import CorpusDefaults as CorpusData


@pytest.mark.parametrize("json_str, expected", [
    ('{"key": "value"}', {"key": "value"}),
    ('{"number": 123}', {"number": 123}),
    ('{"bool": true}', {"bool": True}),
])
def test_parse_json_arg_valid(json_str, expected):
    """Test parsing of valid JSON strings."""
    assert parse_json_arg(json_str) == expected

@pytest.mark.parametrize("json_str", [
    '{"key": "value"',
    'key": "value"}',
    '{"key": value}',
])
def test_parse_json_arg_invalid(json_str):
    """Test parsing of invalid JSON strings should raise ValueError."""
    with pytest.raises(ValueError):
        parse_json_arg(json_str)

@pytest.fixture
def args_basic():
    return ["TestCorpus", "This is a test corpus."]

@pytest.fixture
def args_with_options(args_basic):
    return args_basic + [
        '--encoder_id=123',
        '--custom_dimensions={"dimension1": "value1"}',
        '--public=true'
    ]

def test_parse_args_basic(args_basic):
    name, description, options = parse_args(args_basic)
    assert name == "TestCorpus"
    assert description == "This is a test corpus."
    assert options == CorpusData().get_defaults()

def test_parse_args_with_options(args_with_options):
    name, description, options = parse_args(args_with_options)
    expected_options = CorpusData().get_defaults()
    expected_options.update({
        "customDimensions": {"dimension1": "value1"},
        "encoderId": 123,
        "public": True
    })
    assert name == "TestCorpus"
    assert description == "This is a test corpus."
    assert options == expected_options

@pytest.mark.skip(reason="This function does not correctly handle error simulation")
@patch('vectara_cli.commands.create_corpus.print_create_corpus_advanced_help')
@patch('sys.exit')
def test_parse_args_too_few_args(mock_exit, mock_help):
    # Check if help is printed and the process exits when not enough args are provided
    parse_args(["only_one_arg"])
    mock_help.assert_called_once()
    mock_exit.assert_called_once_with(1)

# @patch('vectara_cli.commands.create_corpus.VectaraClient')
# def test_main_with_mocked_client(mock_VectaraClient, args_with_options):
#     """Test `main` function with mocked Vectara client."""
#     # vectara_client_instance = MagicMock()
#     # mock_VectaraClient.return_value
#     main(args_with_options, mock_VectaraClient)
#     # Assert create_corpus was called once with the expected options
#     expected_options = {
#         "customDimensions": {"dimension1": "value1"},
#         "encoderId": 123,
#         "public": True
#     }
#     vectara_client_instance.create_corpus.assert_called_once_with(
#         "TestCorpus", "This is a test corpus.", **expected_options
#     )