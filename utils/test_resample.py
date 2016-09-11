import os
import resample
import pandas as pd

def test_resample_bid_ask():
    path = 'fixtures/bid-ask.csv'
    resample.resample_bid_ask(path)
    new_path = 'fixtures/resampled/bid-ask.csv'
    assert os.path.exists(new_path)
    df = pd.read_csv(new_path,
            header=None,
            names=['name', 'datetime', 'open', 'high', 'low', 'close'],
            parse_dates=[1])
    df.set_index("datetime")
    assert set(df.columns) == set(['datetime', 'open', 'high', 'low', 'close', 'name'])

