import subprocess

def run_llama3(prompt):
    try:
        # Call the ollama command with the llama3 model
        result = subprocess.run(
            ['ollama', 'run', 'llama3'],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Capture the output and errors, if any
        output = result.stdout.decode()
        error = result.stderr.decode()

        if result.returncode != 0:
            print(f"Error: {error}")
        else:
            print(f"Output: {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit llama":
            print("Exiting the conversation.")
            break
        run_llama3(prompt)
