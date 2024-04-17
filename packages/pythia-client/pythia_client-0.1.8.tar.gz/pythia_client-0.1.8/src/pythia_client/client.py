"""A client for interacting with the API.

This module provides a client class for interacting with the API, including
indexing documents, listing them, deleting them, get S3 URL to a document,
querying them and extracting structured json data from text.

Classes:
    APIClient: Client for interacting with the API.
"""

import os
import json
import io
from typing import List, Optional, Literal, Tuple, Union, Dict
from urllib.parse import urljoin
import requests

from .schema import (
    UploadFileResponse,
    GetFileS3Reponse,
    FilterRequest,
    FilterDocStoreReponse,
    DeleteDocResponse,
    QueryRequest,
    QueryResponse,
    DataExtractRequest,
    DataExtractResponse,
    ChatMessage,
    LogIndexingTable,
    AddIntentResponse,
    PredictIntentResponse,
    DeleteIntentResponse,
)


class APIClient:
    """Client for interacting with the API.

    This class provides methods for interacting with the API, including
    indexing documents, listing them, deleting them, get S3 URL to a document,
    querying them and extracting structured json data from text.

    Attributes:
        url: The base URL for the API.
        api-key: The api key for the API.
        files_endpoint: The endpoint for files operation (upload, get).
        indexing_tasks_endpoint: The endpoint for indexing tasks.
        documents_by_filter_endpoint: The endpoint for documents operation by filters.
        documents_by_s3_key_endpoint: The endpoint for documents operation by S3 key.
        search_endpoint: The endpoint for querying.
        data_extraction_endpoint: The endpoint for extracting JSON data from text.
    """

    def __init__(self, url: str, api_key: str):
        """Initializes the API client with the given URL and the API key.

        Args:
            url: The base URL for the API.
            api_key: The api key for the API.

        Usage:
        ```python
        from pythia_client.client import APIClient
        client = APIClient("http://localhost:8000", "api-key")
        ```
        """
        self.url = url
        self.api_key = api_key
        self.files_endpoint = urljoin(str(self.url), "files")
        self.indexing_tasks_endpoint = urljoin(str(self.url), "files/indexing-tasks")
        self.documents_by_filter_endpoint = urljoin(str(self.url), "documents/filters")
        self.documents_by_s3_key_endpoint = urljoin(str(self.url), "documents/s3-key")
        self.search_endpoint = urljoin(str(self.url), "search/query")
        self.data_extraction_endpoint = urljoin(
            str(self.url), "/data_extraction/extract-structured-data"
        )
        self.add_intent_endpoint = urljoin(str(self.url), "alie/intent")
        self.predict_intent_endpoint = urljoin(str(self.url), "alie/intent/predict")
        self.delete_intent_endpoint = urljoin(str(self.url), "alie/intent")

    def query(
        self,
        query: str,
        chat_history: Optional[List[ChatMessage]] = None,
        filters: Optional[FilterRequest] = None,
        group_id: str = None,
        custom_system_prompt: str = None,
    ) -> QueryResponse:
        """Query the API with a user question to get a LLM-generated answer based
            on context from the document store.

            Args:
                query: The user question to be answered.
                chat_history: The chat history to provide context to the model. Should be a list of ChatMessage objects.
                filters: Haystack 2.0 filter dict. See: https://docs.haystack.deepset.ai/v2.0/docs/metadata-filtering#filters for more information about how to build a filter.
                group_id: The name of the group_id the client making the request, for logging in DynamoDB. Defaults to "api".

            Returns:
                The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

            Usage:
            ```python
            filters = {
                        "operator": "AND",
                        "conditions": [
                            {
                                "field": "meta.source",
                                "operator": "==",
                                "value": "Salesforce",
                            },
                        ],
                    }
            query_response = client.query("Hey how are you", filters=filters)
            query_response.model_dump()
            ```
            Can also be used with chat history:
            ```python
            chat_history = [
                {
                    "content": "Hello Chatbot. My name is Corentin !",
                    "role": "user",
                    "name": None,
                    "meta": {},
                }
            ]
            response = client.query(
                query="Given our previous exchange of messages, what is my name ?",
                chat_history=chat_history,
            )
        ```
        """
        params = FilterRequest(filters=filters).model_dump()
        if custom_system_prompt:
            params["system_prompt"] = custom_system_prompt
        params["group_id"] = group_id if group_id else "api"
        request = QueryRequest(
            query=query,
            chat_history=chat_history,
            params=params,
        )
        with requests.Session() as session:
            payload = json.loads(request.model_dump_json())
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "X-API-Key": self.api_key,
            }
            with session.post(
                self.search_endpoint, headers=headers, json=payload
            ) as response:
                if response.status_code == 200:
                    api_response = QueryResponse(**response.json())
                else:
                    api_response = None
        return api_response

    def upload_files(
        self,
        files: List[Union[str, Tuple[str, io.IOBase]]],
        meta: Optional[List[dict]] = None,
        indexing_mode: Literal["unstructured", "pypdf"] = "unstructured",
    ) -> UploadFileResponse:
        """Index one or multiples files (documents) to the document store through the Haystack-API upload-file endpoint.

        Args:
            files: The paths to the files OR tuples of filename and file object to index.
            meta: The list of metadata for the files.
            indexing_mode: The indexing mode between unstructured and pypdf.

        Returns:
            The response from the API. Returns None if the status code is not 202.

        Usage:
        ```python
        index_response = client.upload_files(["path/to/file.pdf"], meta=[{"source": "Salesforce"}], indexing_mode="pypdf")
        {"message": "Files Submitted. Indexing task created."}
        index_response = client.upload_files([("file.pdf", file)], meta=[{"source": "Salesforce"}], indexing_mode="pypdf")
        {"message": "Files Submitted. Indexing task created."}
        ```
        """
        prepared_files = []
        for file in files:
            if isinstance(file, str):
                file_name = os.path.basename(file)
                with open(file, "rb") as f:
                    file_content = f.read()
            elif (
                isinstance(file, tuple)
                and len(file) == 2
                and isinstance(file[1], io.IOBase)
            ):
                file_name, file_object = file
                file_content = file_object.read()
            else:
                raise ValueError(
                    "Each file must be a file path or a tuple of (filename, fileIObyte)"
                )

            prepared_files.append(("files", (file_name, file_content)))

        with requests.Session() as session:
            payload = {"meta": json.dumps(meta), "indexing_mode": indexing_mode}
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.post(
                self.files_endpoint,
                files=prepared_files,
                data=payload,
                headers=headers,
            ) as response:
                if response.status_code == 202:
                    api_response = response.json()
                else:
                    api_response = None
        return api_response

    def get_indexing_tasks_by_group_id(
        self, group_id: str, top: int = 20
    ) -> List[dict]:
        """Get the indexing tasks from the API.

        Args:
            group_id: The name of the group_id the client making the request, for logging in DynamoDB. If none, the default group_id is "api" (set by the API itself).
            top: The number of top most recent indexing tasks to return.

        Returns:
            The response from the API. Returns None if the status code is not 200.

        Usage:
        ```python
        indexing_tasks = client.get_indexing_tasks(group_id="api", top=20)
        indexing_tasks.model_dump()
        ```
        """
        with requests.Session() as session:
            params = {"top": top}
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.get(
                self.indexing_tasks_endpoint + "/" + group_id,
                params=params,
                headers=headers,
            ) as response:
                if response.status_code == 200:
                    api_response = [
                        LogIndexingTable(**resp) for resp in response.json()
                    ]
                else:
                    api_response = None
        return api_response

    def get_indexing_task_by_s3_key(self, group_id: str, s3_key: str) -> dict:
        with requests.Session() as session:
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.get(
                self.indexing_tasks_endpoint + "/" + group_id + "/" + s3_key,
                headers=headers,
            ) as response:
                if response.status_code == 200:
                    api_response = LogIndexingTable(**response.json())
                else:
                    api_response = None
        return api_response

    def get_file_url(self, s3_key: str, page: Optional[int] = 1) -> GetFileS3Reponse:
        """Get a presigned URL to a file located on S3.

        Args:
            s3_key: The filename of the file to get.
            page: The page to directly point the URL.

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

        Usage:
        ```python
        get_doc_response = client.get_file_url("s3fd_sample.pdf", page=2)
        s3_url = get_doc_response.url
        ```
        """
        with requests.Session() as session:
            params = {"page": page}
            url = self.files_endpoint + "/" + s3_key
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.get(
                url,
                params=params,
                headers=headers,
            ) as response:
                if response.status_code == 200:
                    api_response = GetFileS3Reponse(**response.json())
                else:
                    api_response = None
        return api_response

    def get_docs_by_filters(
        self,
        filters: FilterRequest = None,
        return_content: bool = False,
    ) -> List[FilterDocStoreReponse]:
        """List all documents in the document store that match the filter provided.

        Args:
            filters: Haystack 2.0 filter dict. See: https://docs.haystack.deepset.ai/v2.0/docs/metadata-filtering#filters for more information about how to build a filter.
            return_content: If True, the content of the documents will be returned.

        Returns:
            The response from the API. Returns None if the status code is not 200.

        Usage:
        ```python
        filters = {
                    "operator": "AND",
                    "conditions": [
                        {
                            "field": "meta.source",
                            "operator": "==",
                            "value": "Salesforce",
                        },
                    ],
                }
        list_response = client.get_docs_by_filters(filters=filters)
        list_response.model_dump()
        ```
        """
        request = FilterRequest(filters=filters)
        with requests.Session() as session:
            payload = json.loads(request.model_dump_json())
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "X-API-Key": self.api_key,
            }
            if return_content:
                endpoint = f"{self.documents_by_filter_endpoint}?return_content=true"
            else:
                endpoint = self.documents_by_filter_endpoint

            with session.post(endpoint, headers=headers, json=payload) as response:
                if response.status_code == 200:
                    responses = response.json()
                    api_response = [FilterDocStoreReponse(**resp) for resp in responses]
                else:
                    api_response = None
        return api_response

    def delete_docs_by_filters(
        self,
        filters: FilterRequest = None,
    ) -> DeleteDocResponse:
        """Remove documents from the API document store.

        Args:
            filters: Haystack 2.0 filter dict. See: https://docs.haystack.deepset.ai/v2.0/docs/metadata-filtering#filters for more information about how to build a filter.

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.
        Usage:
        ```python
        filters = {
                    "operator": "AND",
                    "conditions": [
                        {
                            "field": "meta.source",
                            "operator": "==",
                            "value": "Salesforce",
                        },
                    ],
                }
        remove_response = client.delete_docs_by_filters(filters=filters)
        remove_response.model_dump()
        ```
        """
        request = FilterRequest(filters=filters)
        with requests.Session() as session:
            payload = json.loads(request.model_dump_json())
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "X-API-Key": self.api_key,
            }
            with session.delete(
                self.documents_by_filter_endpoint, headers=headers, json=payload
            ) as response:
                if response.status_code == 200:
                    api_response = DeleteDocResponse(**response.json())
                else:
                    api_response = None
        return api_response

    def get_docs_by_s3_key(self, s3_key: str):
        with requests.Session() as session:
            url = self.documents_by_s3_key_endpoint + "/" + s3_key
            headers = {"X-API-Key": self.api_key}
            with session.get(url, headers=headers) as response:
                if response.status_code == 200:
                    api_response = [
                        FilterDocStoreReponse(**resp) for resp in response.json()
                    ]
                else:
                    api_response = None
        return api_response

    def delete_docs_by_s3_key(self, s3_key: str):
        with requests.Session() as session:
            url = self.documents_by_s3_key_endpoint + "/" + s3_key
            headers = {"X-API-Key": self.api_key}
            with session.delete(url, headers=headers) as response:
                if response.status_code == 200:
                    api_response = DeleteDocResponse(**response.json())
                else:
                    api_response = None
        return api_response

    def extract_structured_data(
        self,
        text_content: str,
    ) -> DataExtractResponse:
        """Query the API to extract structured JSON from unstructured text.

        Args:
            text_content: The text to process.

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

        Usage:
        ```python
        extract_response = client.extract_structured_data("Hello I want to modify the delivery date of order FR73681920")
        extract_response.model_dump()
        ```
        """
        request = DataExtractRequest(
            email_content=text_content,
        )
        with requests.Session() as session:
            payload = json.loads(request.model_dump_json())
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "X-API-Key": self.api_key,
            }
            with session.post(
                self.data_extraction_endpoint, headers=headers, json=payload
            ) as response:
                if response.status_code == 200:
                    response = DataExtractResponse(**response.json())
                else:
                    response = None
        return response

    def add_intent(
        self,
        intent_data: Dict[str, List[str]],
    ) -> AddIntentResponse:
        """Add intent data to the intent prediction engine.

        Args:
            intent_data: Dict containing intent data.

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

        Usage:
        ```python
        intent_data = {"greet": ["Hey", "Hello", "Bonjour"], "help": ["I need help", "Show help"]}
        add_intent_response = client.add_intent(intent_data)
        add_intent_response.model_dump()
        ```
        """
        with requests.Session() as session:
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.post(
                self.add_intent_endpoint, headers=headers, data=json.dumps(intent_data)
            ) as response:
                if response.status_code == 200:
                    response = AddIntentResponse(**response.json())
                else:
                    response = None
        return response

    def predict_intent(
        self,
        user_msg: str,
    ) -> PredictIntentResponse:
        """Query the API to predict the intent of a user message.

        Args:
            user_msg: The content of the user message.

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

        Usage:
        ```python
        intent = client.predict_intent("Hello I want to modify the delivery date of order FR73681920")
        intent.model_dump()
        ```
        """
        with requests.Session() as session:
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.get(
                self.predict_intent_endpoint, headers=headers, params={"user_message": user_msg}
            ) as response:
                if response.status_code == 200:
                    response = PredictIntentResponse(**response.json())
                else:
                    response = None
        return response

    def delete_intent(
        self,
        intent_name: str,
    ) -> DeleteIntentResponse:
        """Delete the specified intent from the database. Use "*" to delete all intents from the databse (clear the DB).

        Args:
            intent_name: The name of the intent to delete. Use "*" to delete all intents from the databse (clear the DB).

        Returns:
            The response from the API as a Pydantic model. You can use reponse.model_dump() to get a Dict. Returns None if the status code is not 200.

        Usage:
        ```python
        delete_intent_response = client.delete_intent("greet")
        delete_intent_response.model_dump()
        ```
        """
        with requests.Session() as session:
            headers = {
                "X-API-Key": self.api_key,
            }
            with session.delete(
                self.delete_intent_endpoint, headers=headers, params={"intent_name": intent_name}
            ) as response:
                if response.status_code == 200:
                    response = DeleteIntentResponse(**response.json())
                else:
                    response = None
        return response