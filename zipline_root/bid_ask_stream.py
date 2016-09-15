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
import numpy as np
from utils import resample
from zipline.utils.cli import maybe_show_progress

def ingest(environ,
        asset_db_writer,
        minute_bar_writer,
        daily_bar_writer,
        adjustment_writer,
        calendar,
        start_session,
        end_session,
        cache,
        show_progress,
        output_dir):

    path = environ.get('BID_ASK_STREAM_CSV_FOLDER')
    instruments = os.listdir(path) # get ["EURSD", "AUDUSD"]
    metadata = pd.DataFrame(np.empty(len(instruments), dtype=[
        ('start_date',      'datetime64[ns]'),
        ('end_date',        'datetime64[ns]'),
        ('auto_close_date', 'datetime64[ns]'),
        ('exchange',        'object'),
        ('symbol',          'object'),
        ]))

    def _minute_iter(path):
        """ Yields (sid, dataframe) for ingesting, while updating
        metadata as a closure

        Parameters
        ----------
        path : str
            The path to a folder containing sub folder of instruments,
            which in turn contain ohlc directory. For example:
            /path:
              - /EURUSD:
                  - 06.csv
              - /AUDUSD
                  - 06.csv
        Returns
        -------
        Yield (sid, dataframe)

        Note
        ----
        sid is index of insturment folder in the path. No special meaning.
        """
        pytest.set_trace
        instruments = os.listdir(path) # get ["EURSD", "AUDUSD"]
        for index, name in enumerate(instruments):
            metadata.ix[index] = None, None, None, 'forex', name
            current_dir = os.path.join(path, name)
            # zips = filter(lambda x: ".zip" in x, os.listdir(current_dir))
            # for z in zips:
                # zfile = zipfile.ZipFile(os.path.join(current_dir, z), 'r')
                # zfile.extractall(current_dir)
            csvs = filter(lambda x: ".csv" in x, os.listdir(current_dir))
            with maybe_show_progress(
                    csvs,
                    show_progress,
                    label='Ingesting csv stream for %s: ' % name) as it:
                for minute_csv in csvs:
                    ohlc = resample.bid_ask_to_ohlc(os.path.join(current_dir, minute_csv))

                    # Keep metadata updated
                    if metadata.ix[index, "start_date"] is None or metadata.ix[index, "start_date"] > ohlc.index[0]:
                        metadata.ix[index, "start_date"] = ohlc.index[0]
                    if metadata.ix[index, "end_date"] is None or metadata.ix[index, "end_date"] > ohlc.index[1]:
                        metadata.ix[index, "end_date"] = ohlc.index[1]
                        metadata.ix[index, "auto_close_date"] = ohlc.index[1] + pd.Timedelta(days=1)
                    yield index, ohlc

    pytest.set_trace()
    minute_bar_writer.write(_minute_iter(path), show_progress)
    asset_db_writer.write(metadata)

