# ./commands/span_text.py

import argparse
import json

from vectara_cli.rebel_span.noncommercial.nerdspan import Span
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.core import VectaraClient, LocalVectaraClient
from vectara_cli.rebel_span.noncommercial.nerdspan import Span
import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def main(vectara_client: VectaraClient, args=None):
    parser = argparse.ArgumentParser(description='Process text using Vectara CLI')
    parser.add_argument('--text', type=str, default="the lazy fox jumped over the brown dog", help='The text to analyze')
    parser.add_argument('--model_name', type=str, default='fewnerdsuperfine', help='The name of the model to use')
    parser.add_argument('--model_type', type=str, default='span_marker', help='The type of the model')
    parsed_args = parser.parse_args(args)

    try:
        span_processor = Span(vectara_client, parsed_args.text, parsed_args.model_name, parsed_args.model_type)
        output_str, key_value_pairs = span_processor.analyze_text()
        print(output_str)
        print(json.dumps(key_value_pairs))
    except Exception as e:
        logging.error("Failed in processing text: %s\n%s", str(e), traceback.format_exc())
        print("Error processing text:", str(e))

if __name__ == "__main__":
    main()
