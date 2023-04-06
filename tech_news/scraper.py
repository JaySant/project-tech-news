import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    sel_element = Selector(text=html_content)
    urls = sel_element.css('.next::attr(href)').get()
    if urls:
        return urls
    else:
        None


# Requisito 4
def scrape_news(html_content):
    sel_element = Selector(text=html_content)

    url = sel_element.css("link[rel='canonical']::attr(href)").get()
    title = sel_element.css('.entry-title::text').get().strip()
    timestamp = sel_element.css('li.meta-date::text').get()
    writer = sel_element.css('span.author > a::text').get()
    reading_time = int(sel_element.css('li.meta-reading-time::text').get(
        )[0:2])
    summary = "".join(
        sel_element.css('.entry-content > p:first-of-type *::text').getall(
        )).strip()
    category = sel_element.css('a.category-style > span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    next_page_url = "https://blog.betrybe.com"
    news_list = []

    while next_page_url and len(news_list) < amount:
        response = fetch(next_page_url)
        update_links = scrape_updates(response)
        for link in update_links:
            if len(news_list) < amount:
                fetch_link = fetch(link)
                news_list.append(scrape_news(fetch_link))
            else:
                break
        next_page_url = scrape_next_page_link(response)
    create_news(news_list)
    return news_list
