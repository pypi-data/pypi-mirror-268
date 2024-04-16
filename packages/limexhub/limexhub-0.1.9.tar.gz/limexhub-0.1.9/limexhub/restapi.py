import requests
import pandas as pd
from typing import Optional,Dict
from datetime import datetime

 
class RestAPI:
    def __init__(self, base_url="https://hub.limex.com/v1", token=None):
        self.base_url = base_url
        self.token = token
 
    def _get(self, endpoint, params: Dict):
        params['token'] = self.token
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def instruments(self, assets=None):
        endpoint = "instruments"
        params = {'assets': assets}
        return pd.DataFrame(self._get(endpoint, params=params))
   
    def candles(self, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d'), timeframe=3):
        endpoint = "candles"
        params = {'symbol': symbol, 'from': from_date, 'to': to_date, 'timeframe': timeframe}
        res = pd.DataFrame(self._get(endpoint, params=params))
        if timeframe>=3:
            res['ts'] = pd.to_datetime(res['ts'], utc=True).dt.date
        else:
            res['ts'] = pd.to_datetime(res['ts'], utc=True)
        res = res.sort_values(by=['ts'])
        res = res.set_index('ts')
        return res
   
    def fundamental(self, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d'), fields='ebitda'):
        endpoint = "fundamental"
        params = {'symbol': symbol, 'from': from_date,'to': to_date, 'fields': fields}
        res = pd.DataFrame(self._get(endpoint, params=params))
        res['date'] = pd.to_datetime(res['date'], utc=True).dt.date
        return res
   
    def news(self, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d')):
        endpoint = "news"
        params = {'symbol': symbol, 'from': from_date,'to': to_date}
        res = pd.DataFrame(self._get(endpoint, params=params))
        res['created'] = pd.to_datetime(res['created'], utc=True)
        return res
   
    def events(self, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d'), event_type='dividends'):
        endpoint = "events"
        params = {'symbol': symbol, 'from': from_date, 'to': to_date,'type': event_type}
        res = pd.DataFrame(self._get(endpoint, params=params))
        res['buy_date'] = pd.to_datetime(res['buy_date'], utc=True).dt.date
        return res
   
    def signals(self, vendor, model, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d')):
        endpoint = "signals"
        params = {'vendor': vendor, 'model': model, 'symbol': symbol, 'from': from_date,'to': to_date}
        res = pd.DataFrame(self._get(endpoint, params=params))
        res['trade_date'] = pd.to_datetime(res['trade_date'], utc=True).dt.date
        res = res.set_index('trade_date')
        return res
 
    def models(self, vendor='boosted'):
        endpoint = "models"
        params = {'vendor': vendor}
        return self._get(endpoint, params=params)

    def altercandles(self, symbol, from_date='2020-01-01',to_date=datetime.today().strftime('%Y-%m-%d'), timeframe=3):
        endpoint = "altercandles"
        params = {'symbol': symbol, 'to': to_date, 'from': from_date, 'timeframe': timeframe}
        res = pd.DataFrame(self._get(endpoint, params=params))
        if timeframe>=3:
            res['ts'] = pd.to_datetime(res['ts'], utc=True).dt.date
        else:
            res['ts'] = pd.to_datetime(res['ts'], utc=True)
        return res.sort_values(by=['ts'])
 