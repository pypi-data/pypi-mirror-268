"""
# =============================================================================
#
#  Licensed Materials, Property of Ralph Vogl, Munich
#
#  Project : stocksdatabase
#
#  Copyright (c) by Ralph Vogl
#
#  All rights reserved.
#
#  Description:
#
#  a simple library to handle ohlcv data in a database environment
#
# =============================================================================
"""

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
from financefunctions.dataframes import FinanceFunctionsDataFrame
from financefunctions.functions import cagr, momentum_value, norm
from financefunctions.series import FinanceFunctionsSeries

__all__ = [
    "FinanceFunctionsDataFrame",
    "FinanceFunctionsSeries",
    "cagr",
    "norm",
    "momentum_value",
]
