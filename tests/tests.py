import pytest
import requests.exceptions
import responses
import unittest
import unittest.mock as mock

from pycoingecko import CoinGeckoAPI
from requests.exceptions import HTTPError

class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_get_coins_markets(self):
        # Arrange
        
        markets_json_sample = [ { 'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 48294, 'market_cap': 907779379110, 'market_cap_rank': 1, 'fully_diluted_valuation': 1012957237338, 'total_volume': 28346025056, 'high_24h': 48887, 'low_24h': 46989, 'price_change_24h': 637.45, 'price_change_percentage_24h': 1.3376, 'market_cap_change_24h': 9348990475, 'market_cap_change_percentage_24h': 1.04059, 'circulating_supply': 18819518.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -25.56706, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 71035.18695, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-18T17:28:54.193Z'}, {'id': 'ethereum', 'symbol': 'eth', 'name': 'Ethereum', 'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880', 'current_price': 3450.13, 'market_cap': 404658104949, 'market_cap_rank': 2, 'fully_diluted_valuation': None, 'total_volume': 17025046686, 'high_24h': 3537.22, 'low_24h': 3371.99, 'price_change_24h': -1.225783226741, 'price_change_percentage_24h': -0.03552, 'market_cap_change_24h': -2619729534.5374756, 'market_cap_change_percentage_24h': -0.64323, 'circulating_supply': 117576774.499, 'total_supply': None, 'max_supply': None, 'ath': 4356.99, 'ath_change_percentage': -21.0085, 'ath_date': '2021-05-12T14:41:48.623Z', 'atl': 0.432979, 'atl_change_percentage': 794777.62193, 'atl_date': '2015-10-20T00:00:00.000Z', 'roi': {'times': 94.46563082890877, 'currency': 'btc', 'percentage': 9446.563082890878}, 'last_updated': '2021-09-18T17:29:08.286Z' } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          json = markets_json_sample, status = 200)
        # Act
        
        response = CoinGeckoAPI().get_coins_markets('usd')

        ## Assert
        assert response == markets_json_sample

    @responses.activate
    def test_failed_get_coins_markets(self):
        # Arrange
        
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_markets('usd')

    
