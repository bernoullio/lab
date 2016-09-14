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
    This takes a file like above, resamples into minute ohlc bars

    Parameters
    ----------
    path : str
        Path to bid/ask csv data

    Returns
    -------
    ohlc     : the dataframe containing minute bar data
    """
    df = pd.read_csv(path,
            header=None,
            names=['name', 'datetime', 'bid', 'ask'],
            parse_dates=[1])
    df.set_index('datetime', inplace=True)
    df['mid'] = (df['bid']*100000 + df['ask']*100000) // 2
    ohlcv = df.mid.resample('1Min').ohlc()
    ohlcv['volume'] = df.mid.resample('1Min').count()
    return ohlcv

