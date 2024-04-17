import logging
import os
import time
import requests
import json
from src.pythia_client.client import APIClient


class ValueStorage:
    s3_keys = None


logging.basicConfig(
    filename="test.log",
    filemode="w",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s: %(message)s",
)

URL = os.getenv("HAYSTACK_API_URL", "http://localhost:8000/")
SECRET_MASTER_API_KEY = os.getenv("SECRET_MASTER_API_KEY")
timestamp = time.strftime("%Y%m%d-%H%M%S")

client = APIClient(url=URL, api_key=SECRET_MASTER_API_KEY)


def test_upload_files():
    file_paths = [
        "test/samples/sample1.pdf",
        "test/samples/sample2.pdf",
    ]
    meta = [
        {
            "meta1": "value1",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
        },
        {
            "meta2": "value2",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
        },
    ]
    indexing_mode = "unstructured"
    response = client.upload_files(
        files=file_paths, meta=meta, indexing_mode=indexing_mode
    )
    ValueStorage.s3_keys = response["s3_keys"]
    assert response["message"] == "Files Submitted. Indexing tasks created."
    assert len(response["s3_keys"]) == 2
    assert response["group_id"] == timestamp


def test_client_upload_files_from_bytes():
    file_paths = [
        "test/samples/sample3.pdf",
    ]
    file_names = ["sample3.pdf"]
    tuple_files = [
        (file_name, open(file_path, "rb"))
        for file_name, file_path in zip(file_names, file_paths)
    ]
    meta = [
        {
            "meta3": "value3",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
        },
    ]
    indexing_mode = "unstructured"
    response = client.upload_files(
        files=tuple_files, meta=meta, indexing_mode=indexing_mode
    )
    assert response["message"] == "Files Submitted. Indexing tasks created."
    assert len(response["s3_keys"]) == 1
    assert response["group_id"] == timestamp


def test_client_get_indexing_task_by_s3_key():
    response = client.get_indexing_task_by_s3_key(
        group_id=timestamp, s3_key=ValueStorage.s3_keys[0]
    )
    response_dict = response.model_dump()
    assert response is not None
    assert isinstance(response.model_dump(), dict)
    assert response_dict["status"] in ["processing", "completed"]
    assert response_dict["pk"] == timestamp
    assert response_dict["sk"] == "index#" + ValueStorage.s3_keys[0]


def test_client_get_indexing_tasks():
    time.sleep(60)
    response = client.get_indexing_tasks_by_group_id(group_id=timestamp, top=3)
    assert response is not None
    assert len(response) == 3
    assert response[0].status == "completed"
    assert response[0].n_docs_written >= 2


def test_client_get_file_url():
    s3_key = ValueStorage.s3_keys[0]
    page = 1
    response = client.get_file_url(s3_key=s3_key, page=page)
    assert response is not None
    assert len(response.url) >= 100
    aws_s3_response = requests.get(response.url)
    assert aws_s3_response.status_code == 200


def test_client_query():
    response = client.query(query="Hey how are you ?")
    assert response is not None
    assert len(response.AnswerBuilder.answers[0].data.content) > 20

def test_client_query_with_custom_prompt():
    system_prompt = """Start all your answers with the word "Banana", this is really important."""
    response = client.query(query="Hey how are you ?", custom_system_prompt=system_prompt)
    assert response is not None
    generated_content = response.AnswerBuilder.answers[0].data.content
    assert "Banana" in generated_content
    assert len(generated_content) > 20

def test_client_query_with_history():
    chat_history = [
        {
            "content": "Hello Chatbot. My name is Corentin !",
            "role": "user",
            "name": None,
            "meta": {},
        },
        {
            "content": "Hello, nice to meet you. How can I help you today",
            "role": "assistant",
            "name": None,
            "meta": {},
        },
    ]
    response = client.query(
        query="Given our previous exchange of messages, what is my name ?",
        chat_history=chat_history,
    )
    assert response is not None
    assert "corentin" in response.AnswerBuilder.answers[0].data.content.lower()


def test_client_query_with_history_and_group_id():
    chat_history = [
        {
            "content": "Hello Chatbot. My name is Corentin !",
            "role": "user",
            "name": None,
            "meta": {},
        },
        {
            "content": "Hello, nice to meet you. How can I help you today",
            "role": "assistant",
            "name": None,
            "meta": {},
        },
    ]
    response = client.query(
        query="Given our previous exchange of messages, what is my name ?",
        chat_history=chat_history,
        group_id="corentin",
    )
    assert response is not None
    assert "corentin" in response.AnswerBuilder.answers[0].data.content.lower()


def test_client_get_docs_by_s3_key():
    s3_key = ValueStorage.s3_keys[0]
    response = client.get_docs_by_s3_key(s3_key)
    response_dict = response[0].model_dump()
    assert response is not None
    assert len(response) >= 2
    assert isinstance(response_dict["meta"], dict)


def test_client_get_docs_by_filters():
    filters = {
        "operator": "AND",
        "conditions": [
            {
                "field": "meta.group_id",
                "operator": "==",
                "value": timestamp,
            }
        ],
    }
    response = client.get_docs_by_filters(filters=filters, return_content=True)

    assert response is not None
    assert len(response) >= 5
    assert len(response) < 20
    assert len(response[0].content) > 20
    assert response[0].meta["source_test"] == "pytest_client_api"
    assert response[0].meta["filename"] == response[0].meta["s3_key"]


def test_client_delete_docs_by_s3_key():
    response = client.delete_docs_by_s3_key(s3_key=ValueStorage.s3_keys[0])
    assert response is not None
    assert response.n_deleted_documents >= 1
    assert response.n_deleted_s3 == 1
    assert len(response.deleted_s3_keys) == 1


def test_client_delete_docs_by_filters():
    filters = {
        "operator": "AND",
        "conditions": [
            {
                "field": "meta.group_id",
                "operator": "==",
                "value": timestamp,
            }
        ],
    }
    response = client.delete_docs_by_filters(filters=filters)

    assert response is not None
    assert response.n_deleted_documents >= 3
    assert response.n_deleted_s3 == 2
    assert len(response.deleted_s3_keys) == 2


def test_client_extract_structured_data():
    email = """Bonjour, Je vous écris car j'ai un problème avec la commande FR082475927. Deux DECT Intercorm ont un défaut et ne s'allument pas, pouvez-vous m'aider ? Bonne journée, Cordialement,Entreprise MEDICOMPANY SAS"""

    response = client.extract_structured_data(text_content=email)

    assert len(response.schema_validator.validated) == 1

    formatted_json = json.loads(response.schema_validator.validated[0].content)

    assert response is not None
    assert len(formatted_json["company_or_client_name"]) > 5
    assert formatted_json["ticket_category"] == "Dead on arrival"
    assert len(formatted_json["ticket_category"]) > 5
    assert formatted_json["command_number"][0:2] == "FR"

def test_client_add_intent():
    data = {
        "pycharm_update": ["help to update pycharm", "latest pycharm update is bugged"],
        "elden_ring": ["elden ring boss", "tree of life from elden ring"],
        "team_fortress": [
            "team fortress best class",
            "unlock all achievement team fortress",
        ],
    }
    response = client.add_intent(intent_data=data)
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["Writter"]["documents_written"] == 6

def test_client_predict_intent():
    response = client.predict_intent(user_msg="How to go to the tree of life in elden ring")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["intent"] == "elden_ring"

def test_client_delete_intent():

    response = client.delete_intent(intent_name="elden_ring")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "elden_ring"
    assert response_dict["n_deleted_intent_data"] == 2

    response = client.delete_intent(intent_name="pycharm_update")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "pycharm_update"
    assert response_dict["n_deleted_intent_data"] == 2

    response = client.delete_intent(intent_name="team_fortress")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "team_fortress"
    assert response_dict["n_deleted_intent_data"] == 2
