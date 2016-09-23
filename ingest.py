"""
Run this with pandas==0.18.1 for dramataically better performance
`docker-compose run --rm ingest python ingest.py`
"""

import toolbox
import zipline
import os
os.environ['BID_ASK_STREAM_CSV_FOLDER'] = os.environ.get('BID_ASK_STREAM_CSV_FOLDER', 'fixtures/stream')


zipline.data.bundles.ingest('bid_ask_stream', show_progress=True)
