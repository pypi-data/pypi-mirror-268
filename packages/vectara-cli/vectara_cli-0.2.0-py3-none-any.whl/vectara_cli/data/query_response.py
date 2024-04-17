# vectara_cli/data/query_response.py
class QueryResponse:
    def __init__(self, response_item):
        self.text = response_item.get('text', 'No text available')
        self.score = response_item.get('score', 0.0)
        self.metadata = {item['name']: item['value'] for item in response_item.get('metadata', [])}
        self.document_index = response_item.get('documentIndex', -1)
        self.corpus_key = self.parse_corpus_key(response_item.get('corpusKey', {}))
        self.status = self.parse_status(response_item.get('status', []))
        self.summary = self.parse_summary(response_item.get('summary', {}))
        self.metrics = self.parse_metrics(response_item.get('metrics', {}))

    def parse_summary(self, summary):
        return summary.get('text', "No summary available")

    @staticmethod
    def parse_corpus_key(corpus_key):
        return {
            "customer_id": corpus_key.get('customerId', 'Unknown'),
            "corpus_id": corpus_key.get('corpusId', 'Unknown'),
            "semantics": corpus_key.get('semantics', 'DEFAULT')
        }

    @staticmethod
    def parse_status(statuses):
        if not statuses:
            return [{'code': 'OK', 'detail': 'No status available'}]
        return [{'code': status.get('code', 'UNKNOWN'), 'detail': status.get('statusDetail', 'No detail available')} for status in statuses]


    @staticmethod
    def parse_response(response):
        print("Parsing individual response items...")
        return [QueryResponse(item) if isinstance(item, dict) else item for item in response]

    @staticmethod
    def parse_metrics(metrics):
        return {
            "queryEncodeMs": metrics.get('queryEncodeMs', 0),
            "retrievalMs": metrics.get('retrievalMs', 0),
            "userdataRetrievalMs": metrics.get('userdataRetrievalMs', 0),
            "rerankMs": metrics.get('rerankMs', 0)
        }

    def __str__(self):
        return (
            f"Text: {self.text}\n"
            f"Score: {self.score}\n"
            f"Metadata: {self.metadata}\n"
            f"Document Index: {self.document_index}\n"
            f"Corpus Key: {self.corpus_key}\n"
            f"Status: {self.status}\n"
            f"Summary: {self.summary}\n"
            f"Metrics: {self.metrics}\n"
        )
