import os
from toolbox.data import OandaMinutePriceIngest


def ingest(event, context):
    ingest = OandaMinutePriceIngest(os.environ.get("DATABASE_URL"))
    currencies = ["EUR_UDS",
                  "EUR_JPY",
                  "EUR_GBP",
                  "EUR_SGD",
                  "USD_JPY",
                  "USD_SGD",
                  "GBP_USD",
                  "USD_CHF",
                  "AUD_USD",
                  "AUD_SGD",
                  "NZD_USD",
                  "ZAR_JPY"]
    for currency in currencies:
        print("Ingesting {}".format(currency))
        ingest.run("EUR_USD")

if __name__ == "__main__":
    ingest(None, None)
