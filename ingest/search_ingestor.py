def search_web(query, api_key):
    import requests
    res = requests.post('https://google.serper.dev/search', json={'q': query}, headers={'X-API-KEY': api_key})
    return [r['link'] for r in res.json().get('organic', [])]