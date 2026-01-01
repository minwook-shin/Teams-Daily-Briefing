from datetime import datetime
from .news import get_latest_news
from .market import get_stock_price


def build_message_body(market_lines, news_items) -> str:
    """Build the message body.

    Args:
        market_lines: List of market summary strings.
        news_items: List of news items (each item includes `title` and `link`).

    Returns:
        The body string (supports markdown links).
    """
    lines = []
    if market_lines:
        lines.append("Market Summary:")
        lines.extend(market_lines)
        lines.append("\n")
    if news_items:
        lines.append("Top News:")
        for n in news_items:
            lines.append(f"- [{n.get('title')}]({n.get('link')})")
    lines.append(f"\n생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)

__all__ = ["get_latest_news", "get_stock_price", "build_message_body"]
