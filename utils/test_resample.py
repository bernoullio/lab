import os
import pytest
import datetime
import resample
import pandas as pd

def test_bid_ask_to_ohlc():
    path = 'fixtures/bid-ask.csv'
    df = resample.bid_ask_to_ohlc(path)
    assert set(df.columns) == set(['open', 'high', 'low', 'close'])
    assert df.index[0] == datetime.datetime(2016,7,29,20,50,00)

