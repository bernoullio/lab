"""
Reads csv file and ingests into zipline databundle
Example:
    - CSV_FILE=fixtures/eur_usd_m1.csv zipline ingest
"""

from pandas import read_csv

def ohlc_from_csv(file_path):
    df = read_csv(file_path,
            header=None,
            names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'],
            parse_dates=[[0, 1]])
    return df.set_index("date_time")

def ingest(environ,
        asset_db_writer,
        minute_bar_writer,
        daily_bar_writer,
        adjustment_writer,
        calendar,
        cache,
        show_progress,
        output_dir):
# write metadata
    #  asset_db_writer.write(metadata(instrument))
# write minute bars
    for row in ohlc_from_csv(environ.get("CSV_FILE")):
        minute_bar_writer(row, show_progress)
