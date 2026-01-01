import logging
import feedparser

logger = logging.getLogger(__name__)


def get_latest_news(query: str = "IT기술", hl: str = "ko", gl: str = "KR", max_entries: int = 10):
    """Fetch the latest news items from an RSS feed.

    Args:
        query: Search query string (default: "IT기술").
        max_entries: Maximum number of entries to return.

    Returns:
        List[dict]: A list of dicts where each item has `title` and `link`.
    """
    try:
        feed_url = f"https://news.google.com/rss/search?q={query}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
        feed = feedparser.parse(feed_url)
        entries = feed.get("entries", [])[:max_entries]
        results = [
            {"title": e.get("title"), "link": e.get("link")} for e in entries
        ]
        return results
    except Exception as e:
        logger.exception("Failed to fetch news")
        return []
