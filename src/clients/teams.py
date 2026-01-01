import json
import logging
import urllib3

logger = logging.getLogger(__name__)

def create_text_payload(text: str, title: str = "Daily Briefing", theme_color: str = "Accent") -> dict:
    """Create a MessageCard payload for Microsoft Teams.

    Args:
        text: The body text (Markdown is supported).
        title: Card title. Defaults to "Daily Briefing".
        theme_color: Card accent color as a hex string.

    Returns:
        A dict payload suitable for sending to an Incoming Webhook.
    """
    footer = (
        "\n\nThis bot is part of the [Teams-Daily-Briefing]"
        "(https://github.com/minwook-shin/Teams-Daily-Briefing)"
        " open-source project and Incoming Webhooks with Workflows for Microsoft Teams service."
    )
    card_content = {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.4",
        "body": [
            {
                "type": "TextBlock",
                "text": title,
                "size": "Large",
                "weight": "Bolder",
                "color": theme_color
            },
            {
                "type": "TextBlock",
                "text": text,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": footer,
                "size": "Small",
                "isSubtle": True,
                "wrap": True,
                "spacing": "Medium"
            }
        ]
    }

    # Webhook으로 보낼 때는 'message' 타입의 attachment로 감싸는 게 정석입니다.
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": card_content
            }
        ]
    }

def send_to_teams(webhook_url: str, payload: dict):
    """Post the payload to the given Teams webhook URL.

    Args:
        webhook_url: Microsoft Teams incoming webhook URL.
        payload: Dict payload created by `create_text_payload`.

    Raises:
        Any exception is logged and re-raised.
    """
    headers = {"Content-Type": "application/json"}
    try:
        http = urllib3.PoolManager()
        payload = json.dumps(payload)
        headers = {"Content-Type": "application/json"}
        http.request("POST", webhook_url, body=payload, headers=headers)
    except Exception:
        logger.exception("Failed to send payload to Teams")
        raise
