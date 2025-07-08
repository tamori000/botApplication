import pandas as pd
import requests
from datetime import datetime, timedelta, time
import time
import schedule
from pybit.unified_trading import HTTP
import api_decryptor

account = 'backtestAccount2'
session = HTTP(
    testnet=False,
    api_key=api_decryptor.decryption('key', account),
    api_secret=api_decryptor.decryption('secret', account)
    )

def getSpotUSDC():
    params = {'category': 'spot', 'symbol': 'BTCUSDC'}
    response = requests.get(url='https://api.bybit.com/v5/market/tickers', params=params)
    try:
        result = float(response.json().get('result').get('list')[0].get('lastPrice'))
    except:
        result = 0
    return result


def get_account_balance():
    response = session.get_wallet_balance(accountType = "UNIFIED")
    return response

if __name__ == '__main__':
    print(getSpotUSDC())
    print(get_account_balance())

