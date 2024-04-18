"""
# =============================================================================
#
#  Licensed Materials, Property of Ralph Vogl, Munich
#
#  Project : eod2pd
#
#  Copyright (c) by Ralph Vogl
#
#  All rights reserved.
#
#  Description:
#
#  a simple library to quere EODHistoricalData in a multithreaded environment
#
# =============================================================================
"""

import basefunctions

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
from eod2pd.downloader import EOD2PDMESSAGEIDENTIFIER, Downloader
from eod2pd.downloaderfunctions import (
    get_exchanges,
    get_exchanges_symbols,
    get_symbols_dividends,
    get_symbols_prices,
    get_symbols_prices_bulk,
    get_symbols_splits,
    start_jobs_get_exchanges,
    start_jobs_get_exchanges_symbols,
    start_jobs_get_symbols_dividends,
    start_jobs_get_symbols_prices,
    start_jobs_get_symbols_prices_bulk,
    start_jobs_get_symbols_splits,
)

__all__ = [
    "EOD2PDMESSAGEIDENTIFIER",
    "get_exchanges",
    "get_exchanges_symbols",
    "get_symbols_dividends",
    "get_symbols_prices",
    "get_symbols_prices_bulk",
    "get_symbols_splits",
    "start_jobs_get_exchanges",
    "start_jobs_get_exchanges_symbols",
    "start_jobs_get_symbols_dividends",
    "start_jobs_get_symbols_prices",
    "start_jobs_get_symbols_prices_bulk",
    "start_jobs_get_symbols_splits",
]

# register "eod2pd" message handler
basefunctions.default_threadpool.register_message_handler(
    msg_type=EOD2PDMESSAGEIDENTIFIER, msg_handler=Downloader()
)
