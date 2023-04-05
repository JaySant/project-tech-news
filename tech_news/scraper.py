import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers, timeout=2)
        if response.status_code == 200:
            return response.text
        else:
            None
    except (requests.ReadTimeout):
        None


# Requisito 2
def scrape_updates(html_content):
    sel_element = Selector(text=html_content)
    urls = sel_element.css(
        ".entry-header h2 a::attr(href)"
        ).getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
