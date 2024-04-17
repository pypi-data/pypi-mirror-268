# /vectara_cli/commands/advanced_query.py

from vectara_cli.core import VectaraClient
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.data.query_request import ContextConfig, SummaryConfig, QueryRequest
from vectara_cli.helptexts.help_text import advanced_query_help
import json
from vectara_cli.data.query_response import QueryResponse
import sys


def main(vectara_client, args):
    if len(args) < 4:
        advanced_query_help
        return

    query_text = sys.argv[2]
    num_results = int(sys.argv[3])
    corpus_id = sys.argv[4]
    try:
        context_config = json.loads(sys.argv[5]) if len(args) > 3 else '{}'
        summary_config = json.loads(sys.argv[6])  if len(args) > 4 else '{}'
        response = vectara_client.advanced_query(query_text, num_results, corpus_id, context_config, summary_config)
        print(json.dumps(response, indent=4))
    except (ValueError, json.JSONDecodeError, Exception) as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Starting advanced query main...")
    import sys
    main(sys.argv)