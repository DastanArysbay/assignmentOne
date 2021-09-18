# filters out top N cryptocurrencies by market capitalization 
Arysbay Dastan (SE-2004)

# Installation
PyPI

```bash
pip install pycoingecko
```


# Usage

```python
from pycoingecko import CoinGeckoAPI  
aitu = CoinGeckoAPI()
```

or

```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko 
python3 setup.py install
```




# Usage examples

``` >>> aitu.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 48011}}

print(aitu.ping())
{'gecko_says': '(V3) To the Moon!'}

print(aitu.get_coins_markets(ids='tron',vs_currency='usd'))
[{'id': 'tron', 'symbol': 'trx', 'name': 'TRON', 'image': 'https://assets.coingecko.com/coins/images/1094/large/tron-logo.png?1547035066', 'current_price': 0.105217, 'market_cap': 7543418469, 'market_cap_rank': 26, 'fully_diluted_valuation': None, 'total_volume': 1391545240, 'high_24h': 0.109215, 'low_24h': 0.104292, 'price_change_24h': -0.000581146218, 'price_change_percentage_24h': -0.5493, 'market_cap_change_24h': -47045060.2293911, 'market_cap_change_percentage_24h': -0.61979, 'circulating_supply': 71660220128.0, 'total_supply': 100850743812.0, 'max_supply': None, 'ath': 0.231673, 'ath_change_percentage': -54.57272, 'ath_date': '2018-01-05T00:00:00.000Z', 'atl': 0.00180434, 'atl_change_percentage': 5732.74357, 'atl_date': '2017-11-12T00:00:00.000Z', 'roi': {'times': 54.377377428121896, 'currency': 'usd', 'percentage': 5437.737742812189}, 'last_updated': '2021-09-18T20:23:58.068Z'}]
```

