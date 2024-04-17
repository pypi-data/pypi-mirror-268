# ./tests/index_document.py

import pytest
from io import StringIO
import sys
import json
from unittest.mock import MagicMock, patch

def main(args, client):
    if len(args) < 5:
        sys.stdout.write("Usage: [cust_id] [doc_id] [title] [metadata_json] [section_text]\n")
        return
    cust_id, doc_id, title, metadata_json, section_text = args
    try:
        metadata = json.loads(metadata_json)
    except json.JSONDecodeError as e:
        sys.stdout.write(f"Error decoding metadata_json: {str(e)}\n")
        return
    response, success = client.index_document(cust_id, doc_id, title, metadata, section_text)
    if success:
        sys.stdout.write("Document indexed successfully.\n")
    else:
        sys.stdout.write(f"Document indexing failed: {response}\n")

@pytest.fixture
def vectara_client_mock():
    client = MagicMock()
    client.index_document.return_value = ("Mock response", True)
    return client

def test_index_document_success(vectara_client_mock, monkeypatch):
    args = ["1234", "doc01", "My Title", '{"key": "value"}', "Section Text"]
    monkeypatch.setattr(sys, "argv", ["prog_name"] + args)
    output = StringIO()
    monkeypatch.setattr("sys.stdout", output)

    with patch("vectara_cli.core.VectaraClient", return_value=vectara_client_mock):
        main(args, vectara_client_mock)

    assert output.getvalue().strip() == "Document indexed successfully."

def test_index_document_failure(vectara_client_mock, monkeypatch):
    vectara_client_mock.index_document.return_value = ("Mock failure response", False)
    args = ["4321", "doc02", "Failed Title", '{"key": "value"}', "Failed Section Text"]
    monkeypatch.setattr(sys, "argv", ["prog_name"] + args)
    output = StringIO()
    monkeypatch.setattr("sys.stdout", output)

    with patch("vectara_cli.core.VectaraClient", return_value=vectara_client_mock):
        main(args, vectara_client_mock)

    assert output.getvalue().strip() == "Document indexing failed: Mock failure response"

def test_index_document_json_decode_error(monkeypatch):
    args = ["1234", "doc03", "Bad Metadata", '{bad_json: "value"}', "Section Text"]
    monkeypatch.setattr(sys, "argv", ["prog_name"] + args)
    output = StringIO()
    monkeypatch.setattr("sys.stdout", output)

    main(args, MagicMock())  # using a fresh MagicMock as client is not expected to be called

    assert output.getvalue().strip().startswith("Error decoding metadata_json:")

def test_index_document_insufficient_arguments(monkeypatch):
    args = ["1234"]  # Not enough arguments
    monkeypatch.setattr(sys, "argv", ["prog_name"] + args)
    output = StringIO()
    monkeypatch.setattr("sys.stdout", output)

    main(args, MagicMock())  # Client mock is not called, hence not checking its response

    expected_help_snippet = "Usage:"
    actual_output = output.getvalue().strip()
    assert expected_help_snippet in actual_output