import requests
from bs4 import BeautifulSoup
import json

url =  'https://let-me-explain-43808461.hubspotpagebuilder.com/main' 

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def get_html(url):
    response = requests.get(url,headers=HEADERS, verify=False)
    return response.content

def get_css(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    style = soup.find_all('style')
    result = ''
    for item in style:
        result += item.text
    return result


print(get_css(get_html(url), url))