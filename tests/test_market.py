from unittest.mock import MagicMock
from services import market

def test_get_stock_price_success(mocker):
    """주식 정보를 정상적으로 가져오는 경우"""
    
    # yfinance.Ticker 객체 모킹
    mock_ticker = MagicMock()
    mock_ticker.info = {
        "shortName": "Samsung Electronics",
        "regularMarketPrice": 70000
    }

    mocker.patch('src.services.market.yf.Ticker', return_value=mock_ticker)

    tickers = ["005930.KS"]
    results = market.get_stock_price(tickers)

    assert len(results) == 1
    assert results[0]['ticker'] == "005930.KS"
    assert results[0]['name'] == "Samsung Electronics"
    assert results[0]['price'] == 70000

def test_get_stock_price_failure(mocker):
    """주식 정보를 가져오다가 에러가 난 경우"""
    
    mocker.patch('src.services.market.yf.Ticker', side_effect=Exception("API Error"))

    tickers = ["INVALID"]
    results = market.get_stock_price(tickers)

    assert len(results) == 1
    assert results[0]['ticker'] == "INVALID"
    assert results[0]['price'] is None
