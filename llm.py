import requests
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:3b"

def generate_response(prompt, temperature=0.2, max_tokens=500):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens
                }
            },
            timeout=300
        )
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        raise Exception(
            "Cannot connect to Ollama. "
            "Please start Ollama and try again."
        )
    except requests.exceptions.Timeout:
        raise Exception(
            "The model is taking too long to respond. Try again."
        )
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ollama API error: {e}")

    except (KeyError, ValueError):
        raise Exception("Invalid response received from Qwen.")