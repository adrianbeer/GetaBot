import pandas as pd
from binance.client import Client
import datetime

def get_historical_data(symbol, interval, days):
    # Calculate the start time (40 days ago from now)
    start_time = datetime.datetime.now() - datetime.timedelta(days=days)
    start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')

    # Fetch historical klines data
    client = Client()
    klines = client.get_historical_klines(symbol, interval, start_time_str)
    
    # Convert to DataFrame
    klines_df = pd.DataFrame(klines)
    
    # Assign column names
    klines_df.columns = [
        'Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 
        'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 
        'Taker buy quote asset volume', 'Ignore'
    ]
    
    # Data is supplied in UTC+0
    klines_df['Open time'] = pd.to_datetime(klines_df['Open time']/1000, unit = 's', utc=True).dt.tz_convert(tz='Europe/Berlin')
    klines_df['Close time'] = pd.to_datetime(klines_df['Close time']/1000, unit = 's', utc=True).dt.tz_convert(tz='Europe/Berlin')
    
    numeric_columns = [
        'Open', 'High', 'Low', 'Close', 'Volume', 'Quote asset volume',
        'Taker buy base asset volume', 'Taker buy quote asset volume'
    ]
    klines_df[numeric_columns] = klines_df[numeric_columns].apply(pd.to_numeric, axis=1)
    return klines_df


def bot(data: pd.DataFrame):
    cols = ['date', 'open', 'high', 'low', 'close']
    assert sum([col in data.columnsfor for col in cols])

    try:
        pass
        #get_historical_data()...  
    except Exception as e:
        # Error handling in case API call doesn't work?
        pass 
    
    return "EUR" # or # "BTC"