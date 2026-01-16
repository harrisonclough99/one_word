import os
import requests
import json

url  = "http://localhost:11434/api/chat"

def main():

    messages = {
        "model": "gemma3:1b",
        "messages": [{"role": "user", "content": "What is Python?"}]
    }
    
    response = requests.post(url, json=messages, stream=True)

    if response.status_code == 200:
        print("Streaming response from Ollama:")
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                except json.JSONDecodeError:
                    print(f"failed to parse line: {line}")
        print()

if __name__ == "__main__":
    main()