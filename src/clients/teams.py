import json
import logging
import urllib3

logger = logging.getLogger(__name__)

def create_text_payload(text: str, title: str = "Daily Briefing", theme_color: str = "0078D7") -> dict:
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
    return {
        "type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": theme_color,
        "title": title,
        "text": f"{text}{footer}",
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


