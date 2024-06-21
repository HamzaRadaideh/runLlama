import subprocess
from elasticsearch import Elasticsearch
import os

# def search_documents(query):
#     es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
#     response = es.search(
#         index="your_index",
#         body={
#             "query": {
#                 "match": {
#                     "content": query
#                 }
#             }
#         }
#     )
#     return [hit["_source"]["content"] for hit in response["hits"]["hits"]]

def run_llama3(history, prompt): #, context_documents
    try:
        # context = "\n".join(context_documents)
        full_prompt = "\n".join(history + [prompt]) #+ [context]
        
        result = subprocess.run(
            ['ollama', 'run', 'llama3'],
            input=full_prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode()
        error = result.stderr.decode()

        if result.returncode != 0:
            print(f"Error: {error}")
        else:
            print(f"LLaMA: {output}")
            return output.strip()

    except Exception as e:
        print(f"An error occurred: {e}")

def log_conversation(user_input, llama_output):
    log_dir = "output"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, "conversation_log.txt")

    with open(log_file, "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"LLaMA: {llama_output}\n\n")

if __name__ == "__main__":
    conversation_history = []
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit llama":
            print("Exiting the conversation.")
            break
        # context_documents = search_documents(prompt)
        response = run_llama3(conversation_history, prompt) # response = run_llama3(conversation_history, prompt, context_documents)
        conversation_history.append(f"You: {prompt}")
        conversation_history.append(f"LLaMA: {response}")
        log_conversation(prompt, response)
