from unittest.mock import MagicMock
from services import news

def test_get_latest_news_success(mocker):
    """뉴스 데이터를 정상적으로 가져오는 경우 테스트"""
    
    # Mocking data
    mock_entry_1 = {'title': 'News 1', 'link': 'http://news1.com'}
    mock_entry_2 = {'title': 'News 2', 'link': 'http://news2.com'}
    
    mock_feed = MagicMock()
    mock_feed.get.return_value = [mock_entry_1, mock_entry_2]
    
    mocker.patch('src.services.news.feedparser.parse', return_value=mock_feed)

    results = news.get_latest_news(query="Test", max_entries=2)

    assert len(results) == 2
    assert results[0]['title'] == 'News 1'
    assert results[0]['link'] == 'http://news1.com'

def test_get_latest_news_empty(mocker):
    """뉴스 데이터가 없는 경우 테스트"""
    mock_feed = MagicMock()
    mock_feed.get.return_value = []
    
    mocker.patch('src.services.news.feedparser.parse', return_value=mock_feed)

    results = news.get_latest_news()
    assert results == []

def test_get_latest_news_exception(mocker):
    """예외 발생 시 빈 리스트 반환 테스트"""
    mocker.patch('src.services.news.feedparser.parse', side_effect=Exception("Connection Error"))
    
    results = news.get_latest_news()
    assert results == []
