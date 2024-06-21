import os
import subprocess
from datetime import datetime

# Constants
DATA_FOLDER = 'data'
LOG_DIR = 'output'
LOG_FILE = os.path.join(LOG_DIR, 'conversation_log.txt')
LLAMA_BINARY = 'ollama'
LLAMA_SCRIPT = 'llama3'

def setup_data_folder():
    """Ensure the 'data' folder exists for storing user files."""
    try:
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
    except Exception as e:
        raise RuntimeError(f"Error creating data directory: {e}")
    try:
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
    except Exception as e:
        raise RuntimeError(f"Error creating output directory: {e}")

def process_data_file(file_name):
    """Process a specific file in the 'data' folder."""
    file_path = os.path.join(DATA_FOLDER, file_name)
    try:
        if os.path.isfile(file_path):
            # Example: Read and print the content of the file
            with open(file_path, 'r') as f:
                content = f.read()
            print(f"File {file_name} content:\n{content}")
        else:
            print(f"File {file_name} not found in {DATA_FOLDER}")
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

def list_data_files():
    """List all files in the 'data' folder."""
    try:
        files = os.listdir(DATA_FOLDER)
        if files:
            print(f"Files in {DATA_FOLDER}:")
            for file in files:
                print(file)
        else:
            print(f"No files found in {DATA_FOLDER}")
    except Exception as e:
        print(f"Error listing files: {e}")

def run_llama3(history, prompt):
    """Run LLaMA script with given history and prompt."""
    try:
        full_prompt = "\n".join(history + [prompt])
        
        result = subprocess.run(
            [LLAMA_BINARY, 'run', LLAMA_SCRIPT],
            input=full_prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        output = result.stdout.decode()
        error = result.stderr.decode()

        if result.returncode != 0:
            raise RuntimeError(f"LLaMA execution error: {error}")
        
        print(f"LLaMA: {output}")
        return output.strip()

    except Exception as e:
        raise RuntimeError(f"An error occurred in run_llama3: {e}")

def log_conversation(user_input, llama_output):
    """Log user input and LLaMA output to conversation_log.txt."""
    try:
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} You: {user_input}\n")
            f.write(f"{timestamp} LLaMA: {llama_output}\n\n")

    except Exception as e:
        raise RuntimeError(f"Error while logging conversation: {e}")

def main():
    """Main function to run the conversation loop."""
    setup_data_folder()
    conversation_history = []

    try:
        while True:
            prompt = input("You: ")
            if prompt.lower() == "exit llama":
                print("Exiting the conversation.")
                break
            
            response = run_llama3(conversation_history, prompt)
            conversation_history.append(f"You: {prompt}")
            conversation_history.append(f"LLaMA: {response}")
            log_conversation(prompt, response)

    except KeyboardInterrupt:
        print("\nConversation interrupted.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
