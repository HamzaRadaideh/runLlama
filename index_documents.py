import json
from elasticsearch import Elasticsearch

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def index_documents():
    es = Elasticsearch(
        [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
        basic_auth=('elastic', 'ZhqgnHPRo+3qQW6qj3A2'),
        verify_certs=False
    )

    # Load documents from the JSON file
    with open('data/documents.json', 'r') as file:
        documents = json.load(file)

    # Index each document
    for doc in documents:
        es.index(index="your_index", body=doc)

if __name__ == "__main__":
    index_documents()
