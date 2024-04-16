import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    # 주어진 URL의 웹 페이지를 크롤링하여 HTML 내용을 반환
    response = requests.get(url)
    return response.content
