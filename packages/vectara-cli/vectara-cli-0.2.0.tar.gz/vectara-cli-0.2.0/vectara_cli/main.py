# ./main.py

import sys
from vectara_cli.commands import (
    create_corpus,
    nerdspan_upsert_folder,
    index_text,
    index_document,
    advanced_query,
    delete_corpus,
    span_enhance_folder,
    upload_document,
    upload_enriched_text,
    span_text,
    rebel_upsert_folder,
    upload_folder,
    query,
    specialized_query,
)
from vectara_cli.utils.create_ui import create_ui
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.utils.utils import (
    get_vectara_client,
    set_api_keys as set_api_keys_main,
    get_api_keys as get_api_keys_main,
)
from vectara_cli.helptexts.help_text import main_help_text
from typing import Callable, Dict

def get_command_mapping() -> Dict[str,Callable]:
    command_mapping = {
        "index-document": index_document.main,
        "query": query.main,
        "create-corpus": create_corpus.main,
        "delete-corpus": delete_corpus.main,
        "span-text": span_text.main,
        "span-enhance-folder": span_enhance_folder.main,
        "upload-document": upload_document.main,
        "upload-folder": upload_folder.main,
        "upload-enriched-text": upload_enriched_text.main,
        "nerdspan-upsert-folder": nerdspan_upsert_folder.main,
        "rebel-upsert-folder": rebel_upsert_folder.main,
        "index-text": index_text.main,
        "create-ui": create_ui,
        "advanced-query": advanced_query.main,
        "specialized-query": specialized_query,
    }
    return command_mapping


def handle_api_keys(args):
    if len(args) != 2:
        print(
            "Error: set-api-keys requires exactly 2 arguments: customer_id and api_key."
        )
    else:
        set_api_keys_main(*args)
    sys.exit(1)


def display_api_keys():
    """
    Prints the customer ID and API key to the console.
    """
    customer_id, api_key = get_api_keys_main()
    print(f"Customer ID: {customer_id}")
    print(f"API Key: {api_key}")


def handle_command(command, args):
    vectara_client = get_vectara_client()
    command_mapping = get_command_mapping()
    if command in command_mapping:
        if command == "create-ui":
            command_mapping[command]()
        else:
            command_func = command_mapping[command]
            if callable(command_func):
                command_func(vectara_client, args)
            else:
                print(
                    f"vectara: '{command}' is not a vectara command. See 'vectara --help'."
                )
            sys.exit(1)


def handle_help():
    if len(sys.argv) < 2 or sys.argv[1] in ("help", "--help", "-h"):
        main_help_text()
        sys.exit(0)


def main():
    handle_help()
    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "set-api-keys":
        handle_api_keys(args)
    elif command == "get-api-keys":
        display_api_keys()
    else:
        handle_command(command, args)


if __name__ == "__main__":
    main()
