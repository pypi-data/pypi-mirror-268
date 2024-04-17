# ./vectara-cli/core.py

import requests
import json
import os
import logging
from typing import List, Tuple
from .data.corpus_data import CorpusData
from .data.defaults import CorpusDefaults
from .data.query_request import (
    QueryRequest, CorpusKey, ContextConfig, SummaryConfig, 
    ChatRequest , ScaleRequest , SpecialRequest, GrowthRequest
)
from .data.query_response import QueryResponse

class VectaraClient:
    def __init__(self, customer_id, api_key):
        self.base_url = "https://api.vectara.io"
        self.customer_id = str(customer_id)
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "customer-id": str(customer_id),
            "x-api-key": api_key,
        }

    def index_text(
        self,
        corpus_id,
        document_id,
        text,
        context="",
        metadata_json="{}",
        custom_dims=None,
        timeout=30
    ):
        if custom_dims is None:
            custom_dims = []
        try:
            metadata_json_obj = json.loads(metadata_json)
        except json.JSONDecodeError:
            raise ValueError("metadata_json must be a valid JSON string.")
        
        corpus_id = str(corpus_id)
        url = f"{self.base_url}/v1/core/index"
        payload = {
            "customerId": self.customer_id,
            "corpusId": corpus_id,
            "document": {
                "documentId": document_id,
                "metadataJson": json.dumps(metadata_json_obj),
                "parts": [
                    {
                        "text": text,
                        "context": context,
                        "metadataJson": json.dumps(metadata_json_obj),
                        "customDims": custom_dims,
                    }
                ],
                "defaultPartContext": context,
                "customDims": custom_dims,
            },
        }
        try:
            response = requests.post(f"{self.base_url}/v1/core/index", headers=self.headers, json=payload, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            raise

    def query(self, query_text, num_results=10, corpus_id=None):
        url = f"{self.base_url}/v1/query"
        data_dict = {
            "query": [
                {
                    "query": query_text,
                    "num_results": num_results,
                    "corpus_key": [
                        {
                            "customer_id": self.headers["customer-id"],
                            "corpus_id": corpus_id,
                        }
                    ],
                }
            ]
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data_dict))
        if response.status_code != 200:
            print(f"Query failed with status code: {response.status_code}")
            return None
        try:
            print("a")
            response_data = response.json()
            print("response_data: ", response_data)
        except json.JSONDecodeError:
            print("Failed to parse JSON response from query.")
            return None

        return self._parse_query_response(response_data)

    def advanced_query(self, query_text, num_results,  corpus_id, context_config, summary_config):
        url = f"{self.base_url}/v1/query"
        data = {
            "query": [{
                "query": query_text,
                "start": 0,
                "numResults": num_results,
                "contextConfig": context_config,
                "corpusKey": [{
                    #"customerId": self.customer_id,
                    "corpusId": corpus_id
                }],
                "summary": [summary_config]
            }]
        }

        print("Sending request to:", url)
        print("Request data:", json.dumps(data, indent=4)) 
        response = requests.post(url, headers=self.headers, json=data)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response content: {response.text}")
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data: {response.text}"}
    
    def _parse_query_response(self, response_data):
        print("Parsing query response data...")
        responses = []
        if "responseSet" in response_data:
            for response_set in response_data["responseSet"]:
                if 'response' in response_set:
                    processed_responses = QueryResponse.parse_response(response_set['response'])
                    responses.extend(processed_responses)
        return responses    
    
    @staticmethod
    def _extract_response_info(response):
        return {
            "text": response.get("text", ""),
            "score": response.get("score", 0),
            "metadata": response.get("metadata", []),
            "documentIndex": response.get("documentIndex"),
            "corpusKey": response.get("corpusKey", {}),
        }

    def _get_index_request_json(
        self, corpus_id, document_id, title, metadata, section_text
    ):
        """Constructs the JSON payload for a document to be indexed."""
        document = {
            "document_id": document_id,
            "title": title,
            "metadata_json": json.dumps(metadata),
            "section": [
                {"text": section_text},
            ],
        }

        request = {
            "customer_id": self.customer_id,
            "corpus_id": corpus_id,
            "document": document,
        }

        return json.dumps(request)

    def post_query(self, data):
        url = f"{self.base_url}/v1/query"
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def make_specialized_request(self, request):
        if isinstance(request, SpecialRequest):
            query_data = {
                "query": [{
                    "query": request.query,
                    "start": request.start,
                    "numResults": request.num_results,
                    "contextConfig": request.context_config.to_dict(),
                    "corpusKey": [key.to_dict() for key in request.corpus_config],
                    "summary": [request.summary_config.to_dict()]
                }]
            }

            if isinstance(request, ScaleRequest) and hasattr(request, 'lexical_config'):
                query_data['query'][0]['lexicalInterpolationConfig'] = request.lexical_config.to_dict()

            if isinstance(request, ChatRequest) and hasattr(request, 'chat_config'):
                query_data['query'][0]['chat'] = request.chat_config.to_dict()

            return self.post_query(query_data)

    def create_corpus(self, corpus_data: dict):
        url = f"{self.base_url}/v1/create-corpus"
        response = requests.post(url, headers=self.headers, data=json.dumps({"corpus": corpus_data}))
        return self._parse_response(response)

    def _parse_response(self, response):
        if response.status_code == 200:
            try:
                response_data = response.json()
                return {"success": True, "data": response_data}
            except ValueError:
                return {"success": False, "error": "Invalid JSON in response"}
        else:
            try:
                error_data = response.json()
                return {"success": False, "error": error_data}
            except ValueError:
                return {"success": False, "error": f"HTTP Error {response.status_code}: {response.text}"}

    def _get_index_request_json(
        self, corpus_id, document_id, title, metadata, section_text
    ):
        # Construct the document payload
        document = {
            "document_id": document_id,
            "title": title,
            "metadata_json": metadata,  # Pass the dictionary directly if the API expects an object
            "section": [
                {"text": section_text},
            ],
        }

        # Construct the full request payload
        request = {
            "customer_id": self.customer_id,
            "corpus_id": corpus_id,
            "document": document,
        }

        # Convert the request payload to JSON and log it
        json_payload = json.dumps(request)
        print("Constructed JSON payload:", json_payload)  # Log the payload for debugging

        return json_payload


    def index_document(self, corpus_id, document_id, title, metadata, section_text):
        """
        Indexes a document to the specified corpus using the Vectara platform.

        Args:
            corpus_id (int): ID of the corpus to which data needs to be indexed.
            document_id (str): Unique identifier for the document.
            title (str): Title of the document.
            metadata (dict): A dictionary containing metadata about the document.
            section_text (str): The main content/text of the document.

        Returns:
            A tuple containing the response and a boolean indicating success or failure.
        """
        idx_address = f"{self.base_url}/v1/index"
        metadata_json = json.dumps(metadata)  # Convert metadata to a JSON string

        payload = {
            "customerId": self.customer_id,
            "corpusId": corpus_id,
            "document": {
                "documentId": document_id,
                "title": title,
                "metadataJson": metadata_json, 
                "sections": [{
                    "text": section_text
                }]
            }
        }

        try:
            response = requests.post(idx_address, headers=self.headers, json=payload) 
            response.raise_for_status()  

            message = response.json()
            if "status" in message and message["status"]["code"] in ("OK", "ALREADY_EXISTS"):
                logging.info("Document indexed successfully or already exists.")
                return message, True
            else:
                logging.error("Indexing failed with status: %s", message.get("status", {}))
                return message.get("status", {}), False
        except requests.exceptions.HTTPError as e:
            logging.error("HTTP error occurred: %s", e)
            return {"code": "HTTP_ERROR", "message": str(e)}, False
        except requests.exceptions.RequestException as e:
            logging.error("Error during requests to Vectara API: %s", e)
            return {"code": "REQUEST_EXCEPTION", "message": str(e)}, False
        except ValueError as e:
            logging.error("Invalid response received from Vectara API: %s", e)
            return {"code": "INVALID_RESPONSE", "message": "The response from Vectara API could not be decoded."}, False


    def index_documents_from_folder(
        self, corpus_id, folder_path, return_extracted_document=False
    ) -> Tuple[str,bool,requests.request]:
        """Indexes all documents in a specified folder.

        Args:
            corpus_id: The ID of the corpus to which the documents will be indexed.
            folder_path: The path to the folder containing the documents.

        Returns:
            A list of tuples, each containing the document ID and a boolean indicating success or failure.
        """
        results = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            document_id = os.path.splitext(file_name)[0]

            try:
                response, status = self.upload_document(
                    corpus_id,
                    file_path,
                    # document_id=document_id,
                    return_extracted_document=return_extracted_document,
                )
                extracted_chunks:List[str]=[ i['text'] for i in response['document']['section'] ]
                joined_chunks:str = ''.join(extracted_chunks)
                
                # extracted_text = (
                #     response.get("extractedText", "")
                #     if return_extracted_document
                #     else None
                # )
                results.append((document_id, status == "Success", joined_chunks))
                if status != "Success":
                    logging.error(f"Failed to index document {document_id}: {response}")
                else:
                    logging.info(f"Successfully indexed document {document_id}")
            except Exception as e:
                logging.error(f"Error uploading or indexing file {file_name}: {e}")
                results.append((document_id, False, None))

        return results
    
    def alt_index_documents_from_folder(
        self, corpus_id, folder_path, return_extracted_document=False
    # ) -> Tuple[str,requests,requests.request]:
    ) -> Tuple[str,dict,str]:
        """Indexes all documents in a specified folder.

        Args:
            corpus_id: The ID of the corpus to which the documents will be indexed.
            folder_path: The path to the folder containing the documents.

        Returns:
            A list of tuples, each containing the document ID and a boolean indicating success or failure.
        """
        results = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            document_id = os.path.splitext(file_name)[0]

            try:
                response, status = self.upload_document(
                    corpus_id,
                    file_path,
                    # document_id=document_id,
                    return_extracted_document=return_extracted_document,
                )
                extracted_chunks:List[str]=[ i['text'] for i in response['document']['section'] ]
                joined_chunks:str = ''.join(extracted_chunks)
                

                results.append((document_id, response , joined_chunks))
                
                
                if status != "Success":
                    logging.error(f"Failed to index document {document_id}: {response}")
                else:
                    logging.info(f"Successfully indexed document {document_id}")
            except Exception as e:
                logging.error(f"Error uploading or indexing file {file_name}: {e}")
                results.append((document_id, response, ""))

        return results

    def delete_corpus(self, corpus_id):
        """Deletes a specified corpus.

        Args:
            corpus_id: The ID of the corpus to be deleted.

        Returns:
            A tuple containing the response JSON and a boolean indicating success or failure.
        """
        url = f"{self.base_url}/v1/delete-corpus"
        payload = json.dumps({"corpusId": corpus_id})

        try:
            response = requests.post(url, headers=self.headers, data=payload)
            response_json = response.json()

            # Check if the response has a 'status' field and handle accordingly
            if "status" in response_json:
                vectara_status_code = response_json["status"].get("code", "UNKNOWN")
                if vectara_status_code == "OK":
                    logging.info("Corpus deleted successfully.")
                    return response_json, True
                else:
                    logging.error(
                        "Failed to delete corpus with Vectara status code %s, detail: %s",
                        vectara_status_code,
                        response_json["status"].get("statusDetail", "No detail"),
                    )
                    return response_json, False
            else:
                logging.error("Unexpected response format: %s", response.text)
                return response_json, False
        except requests.exceptions.RequestException as e:
            logging.error("Request failed: %s", e)
            return {"error": str(e)}, False

    def upload_document(
        self,
        corpus_id,
        file_path,
        # document_id=None,
        metadata=None,
        return_extracted_document=False,
    ):
        """
        Uploads and indexes a document into a corpus.

        Args:
            corpus_id: The ID of the corpus into which the document should be indexed.
            file_path: The path to the file to be uploaded.
            document_id: Optional. The Document ID to assign to the file.
            metadata: Optional. A dictionary containing user-defined metadata to attach to the document.
            return_extracted_document: Optional. If set to true, the server returns the extracted document.

        Returns:
            A tuple containing the server's response as a JSON object and a status message.
        """
        url = f"{self.base_url}/v1/upload?c={self.customer_id}&o={corpus_id}"
        if return_extracted_document:
            url += "&d=true"

        files = {"file": open(file_path, "rb")}
        if metadata is not None:
            files["doc_metadata"] = (None, json.dumps(metadata), "application/json")

        response = requests.post(
            url,
            headers={
                key: val for key, val in self.headers.items() if key != "Content-Type"
            },
            files=files,
        )

        if response.status_code == 200:
            return response.json(), "Success"
        else:
            try:
                error_response = response.json()
                error_message = error_response.get("message", "Unknown error")
            except json.JSONDecodeError:
                error_message = "Failed to parse error response."

            raise Exception(
                f"Failed to upload document: HTTP {response.status_code} - {error_message}"
            )


class LocalVectaraClient(VectaraClient):
    """
    A client for interacting with the Vectara API using local environment variables
    for authentication.

    Inherits from VectaraClient.

    Attributes:
        base_url (str): The base URL of the Vectara API.
        customer_id (str): The customer ID used for authentication.
        api_key (str): The API key used for authentication.
        headers (dict): The headers to be included in API requests.

    Methods:
        __init__(self, *args, **kwargs): Initializes the client with authentication
            credentials retrieved from environment variables.
        index_text(self, corpus_id, document_id, text, context="", metadata_json="{}",
            custom_dims=None, timeout=30): Indexes text data into the specified corpus.
        query(self, query_text, num_results=10, corpus_id=None): Performs a simple
            text-based query.
        advanced_query(self, query_text, num_results=10, corpus_id=None, context_config=None,
            summary_config=None): Performs an advanced query with optional configuration
            for context and summary.
        create_corpus(self, corpus_data: CorpusData): Creates a new corpus with the
            provided metadata.
        index_document(self, corpus_id, document_id, title, metadata, section_text):
            Indexes a single document into the specified corpus.
        index_documents_from_folder(self, corpus_id, folder_path, return_extracted_document=False):
            Indexes all documents in a specified folder into the specified corpus.
        delete_corpus(self, corpus_id): Deletes the specified corpus.
        upload_document(self, corpus_id, file_path, document_id=None, metadata=None,
            return_extracted_document=False): Uploads and indexes a single document into
            the specified corpus.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the LocalVectaraClient instance with authentication credentials
        retrieved from environment variables.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        self.base_url = "https://api.vectara.io"
        self.customer_id = os.getenv("VECTARA_CUSTOMER_ID")
        self.api_key = os.getenv("VECTARA_API_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "customer-id": str(self.customer_id),
            "x-api-key": self.api_key,
        }

        
    
