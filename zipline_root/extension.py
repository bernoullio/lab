"""
Reads csv file and ingests into zipline databundle
Example:
    - BID_ASK_STREAM_CSV_FOLDER=data/eur_usd_m1.csv zipline ingest -b bid_ask_stream
"""
import bid_ask_stream
from zipline.data.bundles import register

register('bid_ask_stream', bid_ask_stream.ingest)

