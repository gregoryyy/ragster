import requests

def query_ollama(context, question, model='mistral'):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    response = requests.post('http://localhost:11434/api/generate', json={'model': model, 'prompt': prompt})
    return response.json()['response']