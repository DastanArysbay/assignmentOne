from pycoingecko import CoinGeckoAPI
aitu = CoinGeckoAPI()

print("Which  TOP do u wanna see(1-250)")
def func1():
     N = int(input())
     if 1<= N <=250:
             result = aitu.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page=N, page=1,sparkline=False)
             print(result)
     elif N<=0 or N>250:
                         print("try again between 1-250")
func1()

