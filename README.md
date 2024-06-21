# runLlama Project

## Setup Instructions

1. **Install Elasticsearch**:

   - Follow the instructions on the [Elasticsearch website](https://www.elastic.co/downloads/elasticsearch) to install Elasticsearch.

2. **Install Python Dependencies**:

   - Create a virtual environment and install dependencies:
     ```sh
     python -m venv llamaenv
     source llamaenv/bin/activate  # On Windows use `llamaenv\Scripts\activate`
     pip install -r requirements.txt
     ```

3. **Index Sample Documents**:

   - Run the script to index sample documents into Elasticsearch:
     ```sh
     python index_documents.py
     ```

4. **Run the Chatbot**:
   - Start the chatbot:
     ```sh
     python run_llama3.py
     ```

## Usage

- Type your queries into the console.
- Type `exit llama` to end the conversation.

## Project Structure

<!-- cd C:\elasticsearch-8.14.1\bin
.\elasticsearch.bat

python index_documents.py

python run_llama.py -->
