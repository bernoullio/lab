import os
from toolbox.data import OandaMinutePriceIngest


def ingest(event, context):
    ingest = OandaMinutePriceIngest(os.environ.get("DATABASE_URL"))
    ingest.run("EUR_USD")

if __name__ == "__main__":
    ingest(None, None)
