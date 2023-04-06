from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    list = get_collection().aggregate(
        [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
        ]
    )

    if not list:
        return []

    results = []
    for category in list:
        results.append((category["_id"]))
    return results
