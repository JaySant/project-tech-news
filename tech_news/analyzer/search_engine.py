from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = db.news.find(query)
    results = []
    for new in news:
        results.append((new["title"], new["url"]))
    return results


# Requisito 8
def search_by_date(date):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        query = {"timestamp": parsed_date}
        news = db.news.find(query)
        results = []
        for new in news:
            results.append((new["title"], new["url"]))
        return results
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = db.news.find(query)
    results = []
    for new in news:
        results.append((new["title"], new["url"]))
    return results
