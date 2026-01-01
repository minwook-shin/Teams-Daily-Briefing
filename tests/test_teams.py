import json
from unittest.mock import MagicMock
from clients import teams

def test_create_text_payload_structure():
    """Adaptive Card 페이로드 구조 검증"""
    title = "Test Title"
    text = "Test Body"
    payload = teams.create_text_payload(text, title)

    assert payload['type'] == 'message'
    assert 'attachments' in payload
    assert len(payload['attachments']) == 1
    
    card = payload['attachments'][0]['content']
    assert card['type'] == 'AdaptiveCard'
    assert card['version'] == '1.4'
    
    body_elements = card['body']
    assert body_elements[0]['text'] == title  # 제목
    assert body_elements[1]['text'] == text   # 본문

def test_send_to_teams_success(mocker):
    """Teams 웹훅 전송 성공 테스트"""
    mock_http = MagicMock()
    mocker.patch('src.clients.teams.urllib3.PoolManager', return_value=mock_http)

    webhook_url = "https://test.webhook.url"
    payload = {"test": "data"}
    
    teams.send_to_teams(webhook_url, payload)

    mock_http.request.assert_called_once_with(
        "POST",
        webhook_url,
        body=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )
