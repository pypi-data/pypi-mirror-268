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

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
import basefunctions
import pandas as pd

# -------------------------------------------------------------
# DEFINITIONS REGISTRY
# -------------------------------------------------------------


# -------------------------------------------------------------
# DEFINITIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
# VARIABLE DEFINTIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
#  FUNCTION DEFINITIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
# GET DATAFRAMES FROM OUTPUT QUEUE AND JOIN THEM INTO DICTIONARY
# -------------------------------------------------------------
def get_dataframes_from_output_queue(
    dict_result: bool = True, top_ohlc=True, inner_dates: bool = False
) -> pd.DataFrame | dict:
    """
    Receive a list of DataFrames from the message handler.

    Parameters
    ----------
    dict_result : bool
        If True, the result will be a dictionary with the message type as key.
        If False, the result will be a list of DataFrames.
    inner_dates : bool
        If False, the DataFrames will be filled with None for missing dates.
        If True, the DataFrames will be aligned to the newest date.

    Returns
    -------
    dict or DataFrame
        A dictionary of DataFrames if dict_result is True or if there are multiple DataFrames.
        Otherwise, returns a single DataFrame.
    """
    result = {}
    default_threadpool = basefunctions.get_default_threadpool()
    while not default_threadpool.get_output_queue().empty():
        result = result | default_threadpool.get_output_queue().get()
    if dict_result:
        return result
    else:
        if len(result) > 1:
            return create_multiindex_dataframe(
                result=result, top_ohlc=top_ohlc, inner_dates=inner_dates
            )
        else:
            return result[list(result.keys())[0]]


def create_multiindex_dataframe(
    result: dict, top_ohlc: bool = True, inner_dates: bool = False
) -> pd.DataFrame:
    """
    Create a multi-index DataFrame from a dictionary of DataFrames.

    Parameters:
    -----------
    result : dict
        A dictionary of DataFrames.
    top_ohlc : bool
        If True, OHLC will be on level 0 of multi index in DataFrame.
    inner_dates : bool
        If False, the DataFrames will be filled with None for missing dates.
        If True, the DataFrames will be aligned to the newest date.

    Returns:
    --------
    pd.DataFrame
        A multi-index DataFrame containing the DataFrames from the dictionary.
    """
    original_keys_order = ["open", "high", "low", "close", "adjusted_close", "volume"]

    # sort keys if top_ohlc is True
    if top_ohlc:
        keys = result.keys()
    else:
        keys = sorted(result.keys())

    # remove duplicate indices and reindex
    values = [result[key][~result[key].index.duplicated(keep="first")] for key in keys]

    # Concatenate aligned DataFrames with MultiIndex columns
    result = pd.concat(
        values,
        axis=1,
        join="inner" if inner_dates else "outer",
        sort=False,
        keys=[key.upper() for key in keys],
    )

    # swap levels of multiindex columns
    if top_ohlc:
        result = result.swaplevel(axis=1).sort_index(axis=1)
        result = result.reindex(columns=original_keys_order, level=0)

    return result
