# lab

An environment for multiple users to login and research on Jupyter Notebook.

Exposes [Zipline](https://github.com/quantopian/zipline) capable notebooks through [Jupyterhub](https://github.com/jupyterhub/jupyterhub)


# Start hub

`docker-compose build`
`docker-compose up lab`


# Ingest new prices data

- Download stream data from TrueFX and put in fixture/stream as follows:

     fixtures/stream
              ├── EURUSD
              │   ├── EURUSD-2016-06.zip
              │   └── EURUSD-2016-07.zip
              └── GBPUSD
                  ├── GBPUSD-2016-06.zip
                  └── GBPUSD-2016-07.zip

- `docker-compose run --rm ingest`

# Test

`docker-compose run --rm lab py.test`

To run individual pytest:
`docker-comopse run --rm lab py.test zipline_root/utils/test_resample.py:test_bid_ask_to_ohlc`

# TODO

- function to ingest minute data to mysql
- test trailling + no intervention
