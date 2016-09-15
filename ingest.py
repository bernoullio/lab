"""
Run this with pandas==0.18.1 for dramataically better performance
`docker-compose run --rm ingest python ingest.py`
"""

import sys
import os
# append zipline root because this extension needs helper modules from there
sys.path.append(os.environ.get("ZIPLINE_ROOT"))

from zipline_root import bid_ask_stream
from zipline_root.utils.calendars.exchange_calendar_forex import ForexCalendar

import zipline
from zipline.data.bundles import register
from zipline.utils.calendars import register_calendar

register_calendar('forex', ForexCalendar())
register('bid_ask_stream', bid_ask_stream.ingest,
        calendar='forex', minutes_per_day=1440)
os.environ['BID_ASK_STREAM_CSV_FOLDER'] = os.environ.get('BID_ASK_STREAM_CSV_FOLDER', 'fixtures/stream')
zipline.data.bundles.ingest('bid_ask_stream', show_progress=True)

