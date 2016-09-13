"""
Convert other format into ohlc bars
"""
import pandas as pd

import pytest
import os

def bid_ask_to_ohlc(path):
    """
    CSV downloaded from truefx comes in the following format:
        EUR/USD,20160729 20:59:56.418,1.11712,1.11781
        EUR/USD,20160729 20:59:56.421,1.11697,1.11781
        EUR/USD,20160729 20:59:56.752,1.11696,1.11799
    This takes a file like above, resamples into minute ohlc bars,
    and write to ohlc/<filename>.csv

    Parameters
    ----------
    path : str
        Path to bid/ask csv data

    Side-effect
    -----------
    Writes minute ohlc bars to ohlc/<filename>.csv

    Returns
    -------
    metadata_frame : pd.DataFrame
        A dataframe with the following columns:
            start_date     : the first date of data for this asset
            end_date       : the last date of data for this asset
            auto_close_date: end_date + one day
            exchange       : the exchange for the asset; this is always 'forex'
    """
    df = pd.read_csv(path,
            header=None,
            names=['name', 'datetime', 'bid', 'ask'],
            parse_dates=[1])
    df.set_index('datetime', inplace=True)
    df['mid'] = (df['bid']*100000 + df['ask']*100000) // 2
    ohlc = df.mid.resample('1Min').ohlc()

    dirname, filename = os.path.split(path)
    new_dir = dirname + "/ohlc/"

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    new_path = new_dir + filename
    ohlc.to_csv(new_path)

    metadata_frame = pd.DataFrame({
        "start_date":      [ohlc.index[0]],
        "end_date":        [ohlc.index[-1]],
        "auto_close_date": [ohlc.index[-1] + pd.Timedelta(days=1)],
        "exchange":        ["forex"]
        })

    return metadata_frame

