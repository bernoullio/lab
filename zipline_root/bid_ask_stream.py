"""
Reads csv file of streamed bid and ask prices, then ingests into zipline data.bundle
- Set BID_ASK_STREAM_CSV_FOLDER=path, where path contains the following:
        /path:
          - /EURUSD:
              - 06.zip
              - 07.zip
          - /AUDUSD
              - 06.zip
              - 07.zip
          - ...
"""
import os
import zipfile
import pytest
import pandas as pd
from zipline.utils.cli import maybe_show_progress

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

def _minute_iter(path):
    """ Yields (sid, dataframe) for ingesting.

    Parameters
    ----------
    path : str
        The path to a folder containing sub folder of instruments,
        which in turn contain zipped csv files. For example:
        /path:
          - /EURUSD:
              - 06.zip
              - 07.zip
          - /AUDUSD
              - 06.zip
              - 07.zip
    Returns
    -------
    Yield (sid, dataframe)

    Note
    ----
    sid is index of insturment folder in the path. No special meaning.
    """
    instruments = os.listdir(path)
    with maybe_show_progress(
            instruments,
            show_progress,
            label='Importing minute data from csv: ') as it:
        for index, name in enumerate(instruments):
            current_dir = "%s/%s" % (path, i)
            zips = filter(lambda x: ".zip" in x, os.listdir(current_dir))
            for z in zips:
                zfile = zipfile.ZipFile(z, 'r')
                zfile.extract_all()
            csvs = filter(lambda x: ".csv" in x, os.listdir(current_dir))
            for c in csvs:
                yield index, ohlc_from_csv("%s/%s" % (current_dir, c))


def ingest(environ,
        asset_db_writer,
        minute_bar_writer,
        daily_bar_writer,
        adjustment_writer,
        calendar,
        cache,
        show_progress,
        output_dir):

    minute_bar_writer.write(_minute_iter(environ.get("BID_ASK_STREAM_CSV_FOLDER")), show_progress)
    # asset_db_writer.write(metadata(environ.get("BUNDLE_INSTRUMENT"), df))

