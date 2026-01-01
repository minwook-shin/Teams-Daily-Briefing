import os

from services import build_message_body, market, news
from clients import teams as clients


def run():
    webhook = os.getenv("TEAMS_WEBHOOK_URL")
    if webhook:
        webhook = webhook.strip()
    tickers = os.getenv("TARGET_STOCKS")
    if not tickers:
        tickers = "^KS11,^KS200"
        print("No TARGET_STOCKS defined; using defaults: %s", tickers)
    ticker_list = [t.strip() for t in tickers.split(",") if t.strip()]

    market_info = market.get_stock_price(ticker_list)
    market_lines = []
    for m in market_info:
        if m.get("price") is None:
            market_lines.append(f"{m.get('ticker')}: 데이터 없음")
        else:
            market_lines.append(f"{m.get('name')}({m.get('ticker')}): {m.get('price')}")
    body = build_message_body(market_lines, news.get_latest_news())

    payload = clients.create_text_payload(body)
    if webhook:
        clients.send_to_teams(webhook, payload)
    else:
        print("No webhook configured. Payload:\n%s", payload)


if __name__ == "__main__":
    run()
