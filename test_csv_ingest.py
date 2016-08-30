import csv_ingest

def test_ohlc_from_csv():
    df = csv_ingest.ohlc_from_csv('fixtures/eur_usd_m1.csv')
    assert set(df.columns) == set(['open', 'high', 'low', 'close', 'volume'])

