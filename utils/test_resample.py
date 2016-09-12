import os
import pytest
import resample
import pandas as pd

def test_resample_bid_ask():
    path = 'fixtures/bid-ask.csv'
    resample.resample_bid_ask(path)
    new_path = 'fixtures/ohlc/bid-ask.csv'
    assert os.path.exists(new_path)
    df = pd.read_csv(new_path,
            header=1,
            names=['datetime', 'open', 'high', 'low', 'close'],
            parse_dates=[0])
    df.set_index("datetime", inplace=True)
    assert set(df.columns) == set(['open', 'high', 'low', 'close'])

