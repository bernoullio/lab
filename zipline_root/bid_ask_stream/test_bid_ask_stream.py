import os
import pytest
from datetime import datetime, timedelta
import pytz
import pandas as pd
import numpy as np
from . import bid_ask_stream
import zipline
from utils.calendars.exchange_calendar_forex import ForexCalendar
from zipline.data.bundles import register
from zipline.utils.calendars import register_calendar

# @pytest.mark.skip("need pandas 0.17.1, which is prepared with docker-compose service named ingest")
def test_ingest():
    register_calendar('forex', ForexCalendar())
    register('bid_ask_stream',
            bid_ask_stream.ingest,
            calendar='forex',
            start_session= pd.Timestamp(os.environ.get("DATA_START"), tz='utc'),
            end_session= pd.Timestamp(os.environ.get("DATA_END"), tz='utc'),
            minutes_per_day=1440)
    os.environ['BID_ASK_STREAM_CSV_FOLDER'] = 'fixtures/stream'
    zipline.data.bundles.ingest('bid_ask_stream', show_progress=True)
    assert True

def test_df_iloc():
    metadata = pd.DataFrame({
        'start_date': [ datetime.today() ],
        'end_date': [ datetime.today() + timedelta(days=1) ],
        'auto_close_date': [ datetime.today() + timedelta(days=2)],
        'exchange': ['forex'],
        'symbol': ['test']
        })
    assert metadata.iloc[0]["start_date"] < metadata.iloc[0]["end_date"]
    metadata.ix[0, "start_date"] = datetime.today() + timedelta(days=3)
    assert metadata.iloc[0]["start_date"] > metadata.iloc[0]["end_date"]

def test_max_with_tz():
    t = pd.Timestamp.max.replace(tzinfo=pytz.UTC)
    today = datetime.today().replace(tzinfo=pytz.UTC)
    assert t > today

