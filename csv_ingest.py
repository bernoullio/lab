"""
Reads csv file and ingests into zipline databundle
Example:
    - CSV_FILE=fixtures/eur_usd_m1.csv zipline ingest
"""
import pandas as pd

def ohlc_from_csv(file_path):
    df = pd.read_csv(file_path,
            header=None,
            names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'],
            parse_dates=[[0, 1]])
    return df.set_index("date_time")

def metadata(instrument, df):
    start_date = df.index[0]
    end_date = df.index[-1]
    # The auto_close date is the day after the last trade.
    ac_date = end_date + pd.Timedelta(days=1)
    return pd.DataFrame({
        'start_date':      [start_date],
        'end_date':        [end_date],
        'auto_close_date': [ac_date],
        'symbol':          [instrument]})

def csv_ingest(environ,
        asset_db_writer,
        minute_bar_writer,
        daily_bar_writer,
        adjustment_writer,
        calendar,
        cache,
        show_progress,
        output_dir):

    df = ohlc_from_csv(environ.get("CSV_FILE"))

    asset_db_writer.write(metadata(instrument, df))
    for row in df:
        minute_bar_writer(row, show_progress)

