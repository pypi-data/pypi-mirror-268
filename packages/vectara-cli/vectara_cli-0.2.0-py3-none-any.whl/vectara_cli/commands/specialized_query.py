# vectara_cli/commands/specialized_query.py

import json
from argparse import ArgumentParser

from vectara_cli.data.query_request import QueryRequest, ContextConfig, CorpusKey, SummaryConfig, LexicalInterpolationConfig, Dimension, ModelParams

def parse_args(args):
    parser = ArgumentParser(description="Send a specialized query to Vectara platform")
    
    parser.add_argument("type", type=str, choices=['growth', 'scale', 'chat'], help="Type of specialized query")
    parser.add_argument("query_text", type=str, help="The text for the query")
    parser.add_argument("num_results", type=int, help="Number of search results to return")
    parser.add_argument("--corpus_id", type=int, required=True, help="Corpus ID to search in")
    
    # Optional Context Configurations
    parser.add_argument("--chars_before", type=int, default=0, help="Characters before the result snippet")
    parser.add_argument("--chars_after", type=int, default=0, help="Characters after the result snippet")
    parser.add_argument("--sentences_before", type=int, default=0, help="Sentences before the result snippet")
    parser.add_argument("--sentences_after", type=int, default=0, help="Sentences after the result snippet")
    
    # Summary Configurations
    parser.add_argument("--summary_prompt_name", type=str, default="default", help="The prompt name for summarization")
    parser.add_argument("--response_lang", type=str, default="en", help="Response language")

    # Lexical Interpolation
    parser.add_argument("--lambda", type=float, default=0.5, help="Lambda value for lexical interpolation")
    parser.add_argument("--dim_name", type=str, default="relevance", help="Dimension name for interpolation")
    parser.add_argument("--dim_weight", type=float, default=1.0, help="Weight for the dimension")
    
    return parser.parse_args(args)

def handle_request(vectara_client, args):
    context_config = ContextConfig(
        chars_before=args.chars_before,
        chars_after=args.chars_after,
        sentences_before=args.sentences_before,
        sentences_after=args.sentences_after,
        start_tag="<b>",
        end_tag="</b>"
    )
    
    corpus_key = CorpusKey(customer_id=vectara_client.customer_id, corpus_id=args.corpus_id)
    summary_config = SummaryConfig(summarizer_prompt_name=args.summary_prompt_name,
                                   max_summarized_results=args.num_results,
                                   response_lang=args.response_lang)
    
    dimensions = [Dimension(name=args.dim_name, weight=args.dim_weight)]
    
    lexical_config = LexicalInterpolationConfig(lambda_val=args.lambda_val , dimensions=dimensions)
    
    query_request = QueryRequest(
        query=args.query_text,
        start=0,
        num_results=args.num_results,
        context_config=context_config,
        corpus_keys=[corpus_key],
        summary_config=summary_config,
        lexical_interpolation_config=lexical_config
    )
    
    return vectara_client.make_specialized_request(query_request)

def specialized_query(cmd_args, vectara_client):
    args = parse_args(cmd_args)
    response = handle_request(vectara_client, args)
    print("Response from Vectara API:")
    print(json.dumps(response, indent=2))