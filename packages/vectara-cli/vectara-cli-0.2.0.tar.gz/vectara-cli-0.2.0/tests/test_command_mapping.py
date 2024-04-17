# test_command_mapping.py

import pytest
from vectara_cli.main import get_command_mapping

def test_command_mapping():
    expected_commands = [
        "index-document", 
        "query", 
        "create-corpus",
        "delete-corpus",
        "span-text",
        "span-enhance-folder",
        "upload-document",
        "upload-enriched-text",
        "nerdspan-upsert-folder",
        "rebel-upsert-folder",
        "index-text",
        "create-ui",
        "upload-folder"
    ]
    command_mapping = get_command_mapping()
    missing_commands = [cmd for cmd in expected_commands if cmd not in command_mapping]
    assert not missing_commands, f"Commands {missing_commands} are missing in command_mapping"