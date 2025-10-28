import feedparser

def fetch_latest_item(feed_url: str):
    d = feedparser.parse(feed_url)
    if not d.entries:
        return None
    e = d.entries[0]
    return {
        "title": getattr(e, "title", ""),
        "link": getattr(e, "link", ""),
        "guid": getattr(e, "id", "") or getattr(e, "guid", ""),
        "published": getattr(e, "published", ""),
        "summary": getattr(e, "summary", ""),
    }
