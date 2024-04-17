import requests
from selenium import webdriver
from bs4 import BeautifulSoup


def crawl_website(url):
    # 주어진 URL의 웹 페이지를 크롤링하여 HTML 내용을 반환
    response = requests.get(url)
    html_content = response.content

    # HTML 문서 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def open_url(url):
    browser = webdriver.Chrome()
    browser.get(url)

    return browser
