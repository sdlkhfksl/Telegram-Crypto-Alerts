from os import mkdir, getcwd, getenv, listdir
from os.path import isdir, join, dirname, abspath, isfile, exists


"""Alert Handler Configuration"""
POLLING_PERIOD = 10  # Delay for the alert handler to pull prices and check alert conditions (in seconds)
BINANCE_CALL_URL = 'https://api.binance.com/api/v3/ticker/price?symbol={}'

"""Telegram Handler Configuration"""
MAX_ALERTS_PER_USER = 10  # Integer or None (Should be set in a static configuration file)

"""Paths"""
WHITELIST_ROOT = join(dirname(abspath(__file__)), 'whitelist')
RESOURCES_ROOT = join(dirname(abspath(__file__)), 'resources')

"""TAAPI.IO"""
INTERVALS = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "12h", "1d", '1w']
DEFAULT_EXCHANGE = "binance"
