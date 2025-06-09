import requests
from bs4 import BeautifulSoup

def crawl_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.get_text()