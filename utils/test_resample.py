import os
import pytest
import datetime
import resample
import pandas as pd

def test_bid_ask_to_ohlc():
    path = 'fixtures/bid-ask.csv'
    metadata = resample.bid_ask_to_ohlc(path)
    new_path = 'fixtures/ohlc/bid-ask.csv'
    assert os.path.exists(new_path)
    df = pd.read_csv(new_path,
            header=1,
            names=['datetime', 'open', 'high', 'low', 'close'],
            parse_dates=[0])
    df.set_index("datetime", inplace=True)
    assert set(df.columns) == set(['open', 'high', 'low', 'close'])

    assert set(metadata.columns) == set(['start_date', 'end_date', 'auto_close_date', 'exchange'])
    assert metadata.start_date[0] == datetime.datetime(2016,7,29,20,50,00)

