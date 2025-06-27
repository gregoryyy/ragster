import requests
from requests.exceptions import RequestException, Timeout
from config import get_config

def query_ollama(context, question):
    """
    Query Ollama's /api/chat endpoint using RAG context and question.

    Args:
        context (str): The retrieved context for the model.
        question (str): The user input question.

    Returns:
        str: The generated answer or an error message.
    """
    config = get_config()
    model = config.ollama.model
    timeout = int(config.ollama.timeout)
    host = config.ollama.host

    url = f"{host}/api/generate"

    prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        result = response.json()

        if 'response' not in result:
            return "[Error] Ollama response format invalid: missing 'response'"

        return result['response']

    except Timeout:
        return "[Error] Request to Ollama timed out."

    except RequestException as e:
        return f"[Error] Request to Ollama failed: {str(e)}"

    except ValueError:
        return "[Error] Failed to parse Ollama JSON response."


