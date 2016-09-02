# lab

An environment for multiple users to login and research on Jupyter Notebook.

Exposes [Zipline](https://github.com/quantopian/zipline) capable notebooks through [Jupyterhub](https://github.com/jupyterhub/jupyterhub)


# Start hub

`docker-compose build`
`docker-compose up live`


# Test
`docker-compose run --rm test`

To run individual pytest:
`docker-comopse run --rm test py.test zipline_root/test_extension.py`
