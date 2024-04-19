"""
# =============================================================================
#
#  Licensed Materials, Property of Ralph Vogl, Munich
#
#  Project : financefunctions
#
#  Copyright (c) by Ralph Vogl
#
#  All rights reserved.
#
#  Description:
#
#  financefunctions provides functionality for stock prices analysis
#
# =============================================================================
"""

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
import numpy as np
import pandas as pd
import scipy.stats

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
# FUNCTIONS DEFINITIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
# Normalize function
# -------------------------------------------------------------
def norm(df: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """normalize the dataframe to first line

    Returns
    -------
    pandas datafrage
        normalized dataframe to first line
    """
    return df.ff.norm()


# -------------------------------------------------------------
# CAGR function
# -------------------------------------------------------------
def cagr(series: pd.Series) -> float:
    """calculate cagr (compound annual growth rate) of a series.

    Returns
    -------
    float
        float with cagr
    """
    return series.ff.cagr()


# -------------------------------------------------------------
# momentum value
# -------------------------------------------------------------
def momentum_value(series: pd.Series) -> float:
    """calculate momentum of the series with exponential regression.

    Parameters
    ----------
    series : pd.Series
        series to calculate momentum

    Returns
    -------
    float
        momentum value for complete series
    """
    log_data = np.log(series)
    x = np.arange(len(log_data))
    beta, _, rvalue, _, _ = scipy.stats.linregress(x, log_data)
    return (1 + beta) ** 252 * rvalue**2
