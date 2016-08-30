import os
import pytest
import extension
from zipline.data.bundles import ingest

def test_ohlc_from_csv():
    df = extension.ohlc_from_csv('fixtures/eur_usd_m1.csv')
    assert set(df.columns) == set(['open', 'high', 'low', 'close', 'volume'])

def test_metadata():
    df = extension.ohlc_from_csv('fixtures/eur_usd_m1.csv')
    meta = extension.metadata('EURUSD', df)
    assert meta.iloc[0]['symbol'] == 'EURUSD'

def test_ingest():
    ingest('csv')

