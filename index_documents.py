import json
from elasticsearch import Elasticsearch

def index_documents():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Load documents from the JSON file
    with open('data/documents.json', 'r') as file:
        documents = json.load(file)

    # Index each document
    for doc in documents:
        es.index(index="your_index", body=doc)

if __name__ == "__main__":
    index_documents()
