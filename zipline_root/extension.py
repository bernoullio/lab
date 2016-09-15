"""
Reads csv file and ingests into zipline databundle
Example:
    - BID_ASK_STREAM_CSV_FOLDER=data/eur_usd_m1.csv zipline ingest -b bid_ask_stream
"""
import sys
import os
# append zipline root because this extension needs helper modules from there
sys.path.append(os.environ.get("ZIPLINE_ROOT"))

import bid_ask_stream
from zipline.data.bundles import register
from zipline.utils.calendars import register_calendar
from utils.calendars.exchange_calendar_forex import ForexCalendar

register_calendar('forex', ForexCalendar)
register('bid_ask_stream', bid_ask_stream.ingest,
        calendar='forex', minutes_per_day=1440)

