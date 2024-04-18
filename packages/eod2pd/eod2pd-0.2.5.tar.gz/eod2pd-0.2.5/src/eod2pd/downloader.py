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

import queue
import typing
from typing import Any

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
import basefunctions
import basefunctions.threadpool
import pandas as pd
import requests

import eod2pd.downloaderfunctions

# -------------------------------------------------------------
# DEFINITIONS REGISTRY
# -------------------------------------------------------------

# -------------------------------------------------------------
# DEFINITIONS
# -------------------------------------------------------------
EOD2PDMESSAGEIDENTIFIER = "eod2pd"

# -------------------------------------------------------------
# VARIABLE DEFINTIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
#  CLASS DEFINITIONS
# -------------------------------------------------------------
class Downloader(basefunctions.threadpool.ThreadPoolUserObject):
    """
    A class for downloading data from a URL and putting it into an output
    queue.

    Attributes:
        params (dict): A dictionary of parameters for the downloader.

    Methods:
        callable_function(output_queue, item): Downloads data from a URL
        and puts it into the output queue.
        get_params(**kwargs): Get the parameters for the downloader.
        buildResultDataFrame(queue, normalize, dropnaTickers, dropna,
            dropVolume, capitalize, formatStockstats): Builds the result
            dataframe from both offline db and online requests.
    """

    # -------------------------------------------------------------
    # VARIABLE DEFINTIONS
    # -------------------------------------------------------------

    # -------------------------------------------------------------
    #  callable_function method gets called by the threadpool after
    #  a new command has arrived in the input queue. From the class
    #  it's not possible to predict from which thread this function
    #  is called. The function has to be thread safe.
    # -------------------------------------------------------------
    def callable_function(
        self,
        thread_local_data: Any,
        input_queue: queue.Queue,
        output_queue: queue.Queue,
        message: basefunctions.threadpool.ThreadPoolMessage,
    ) -> int:
        """
        Downloads data from a URL and puts it into the output queue.

        Parameters:
            thread_local_data (Any): thread local data.
            input_queue (LifoQueue): The queue to get the parameters from.
            output_queue (Queue): The queue to put the downloaded data into.
            message: ThreadPoolMessage
        Raises:
            ValueError: If item is not a dictionary.
        """
        # check if message.type is of type eod2pd
        if not message.type == EOD2PDMESSAGEIDENTIFIER:
            raise ValueError(f"##FAILURE## message.type is not '{EOD2PDMESSAGEIDENTIFIER}'")
        # get message content
        message_content = typing.cast(
            eod2pd.downloaderfunctions.EOD2PDMessageContent, message.content
        )
        # load data from url without timeout parameter
        result = requests.get(message_content.url, timeout=None)
        # check if status code is 200
        if result.status_code == 200:
            # convert to dataframe
            df = pd.DataFrame(result.json())
            # check for empty dataframe
            if not df.empty:
                # make columns all lowercase in every case
                df.columns = [x.lower() for x in df.columns]
                if message_content.type == "exchanges":
                    pass
                if message_content.type == "exchange-symbols-list":
                    # rename column code to symbol
                    df.rename(columns={"code": "symbol"}, inplace=True)
                    df["symbol"] = df["symbol"].apply(
                        lambda x: f"{x}.{message_content.key}".upper()
                    )
                if message_content.type == "exchange-symbols-prices-bulk":
                    df["date"] = pd.to_datetime(df["date"])
                    df.set_index("date", inplace=True)
                    df.rename(columns={"code": "symbol"}, inplace=True)
                    df["symbol"] = df["symbol"].apply(
                        lambda x: f"{x}.{message_content.key[0]}".upper()
                    )
                    # drop columns exchange_short_name
                    df.drop(columns=["exchange_short_name"], inplace=True)
                if message_content.type == "exchange-symbols-prices":
                    df["date"] = pd.to_datetime(df["date"])
                    df.set_index("date", inplace=True)
                    df.insert(0, "symbol", message_content.key.upper())
                if message_content.type == "exchange-symbols-dividends":
                    df["date"] = pd.to_datetime(df["date"])
                    df.set_index("date", inplace=True)
                    df.insert(0, "symbol", message_content.key.upper())
                if message_content.type == "exchange-symbols-splits":
                    df["date"] = pd.to_datetime(df["date"])
                    df.set_index("date", inplace=True)
                    df.insert(0, "symbol", message_content.key.upper())
        # if status code is 404 return empty dataframe
        elif result.status_code == 404:
            df = pd.DataFrame()
        # otherwise raise an error
        else:
            raise ValueError(f"##FAILURE## result {result.status_code} for {message_content.url}")
        # put it into the output queue
        output_queue.put({message_content.key: df})
        # return result
        return 0
