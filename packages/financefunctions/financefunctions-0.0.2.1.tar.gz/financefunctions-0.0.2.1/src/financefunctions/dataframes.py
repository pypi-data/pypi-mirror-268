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
from typing import List

import numpy as np
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
# FUNCTIONS DEFINITIONS
# -------------------------------------------------------------
@pd.api.extensions.register_dataframe_accessor("ff")
class FinanceFunctionsDataFrame:
    """
    FinanceFunctionsDataFrame class provides additional functionality for
    pandas dataframes. The class is registered as an accessor to the pandas
    dataframe object.
    """

    def __init__(self, pandas_obj: pd.DataFrame) -> None:
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj) -> None | RuntimeError:
        if not isinstance(obj, pd.DataFrame):
            raise RuntimeError(f"expected pandas dataframe object, received {type(obj)}")

    @property
    def freq_factor(self) -> int | RuntimeError:
        """
        get frequence factor value

        Returns
        -------
        int
            frequence factor value to calculate annual returns

        Raises
        ------
        RuntimeError
            raise RuntimeError if frequence is unknown
        """
        freq = pd.Series(self._obj.index).diff().mean().components.days
        if freq == 1:
            return 252
        if freq == 30:
            return 12
        if freq == 365:
            return 1

        raise RuntimeError(f"unknown dataframe frequence {freq}")

    # -------------------------------------------------------------
    # Values, StandardDeviations and Means
    # -------------------------------------------------------------
    def vals_p(self, dropna: bool = False) -> pd.DataFrame:
        """
        return positive values of dataframe

        Parameters
        ----------
        dropna : bool, optional
            drop Nan values, by default False

        Returns
        -------
        pandas dataframe
            pandas dataframe with positive values
        """
        return self._obj[self._obj > 0].dropna() if dropna else self._obj[self._obj > 0]

    def vals_n(self, dropna: bool = False) -> pd.DataFrame:
        """
        return negative values of dataframe

        Parameters
        ----------
        dropna : bool, optional
            drop Nan values, by default False

        Returns
        -------
        pandas dataframe
            pandas dataframe with negative values
        """
        return self._obj[self._obj < 0].dropna() if dropna else self._obj[self._obj < 0]

    def std_p(self, ddof: int = 1) -> pd.Series:
        """
        standard deviation of positive values

        Parameters
        ----------
        ddof : int, optional
            delta degrees of freedom, by default 1 ( standard param from used std-function )

        Returns
        -------
        pandas series
            pandas series with standard deviations of positive values
        """
        return self._obj[self._obj > 0].std(ddof=ddof)

    def std_n(self, ddof: bool = 1) -> pd.Series:
        """
        standard deviation of negative values

        Parameters
        ----------
        ddof : int, optional
            delta degrees of freedom, by default 1 ( standard param from used std-function )

        Returns
        -------
        pandas series
            pandas series with standard deviations of negative values
        """
        return self._obj[self._obj < 0].std(ddof=ddof)

    def mean_p(self) -> pd.Series:
        """
        mean of positive values

        Returns
        -------
        pandas series
            pandas series with mean of positive values
        """
        return self._obj[self._obj > 0].mean()

    def mean_n(self) -> pd.Series:
        """
        mean of negative values

        Returns
        -------
        pandas series
            pandas series with mean of negative values
        """
        return self._obj[self._obj < 0].mean()

    # -------------------------------------------------------------
    # Normalize function
    # -------------------------------------------------------------
    def norm(self) -> pd.DataFrame:
        """normalize dataframe to first line, dataframe can be universal

        Returns
        -------
        pandas dataframe
            normalized dataframe to first line
        """
        # Select numeric columns
        numeric_columns = self._obj.select_dtypes(include="number").columns

        return self._obj[numeric_columns].div(self._obj[numeric_columns].iloc[0]).mul(100)

    # -------------------------------------------------------------
    # columns functions
    # -------------------------------------------------------------
    def subcols(self, cols: str | List[str]) -> pd.DataFrame:
        """
        return subcolumn of dataframe

        Parameters
        ----------
        col : str
            column name

        Returns
        -------
        pandas dataframe
            subcolumns of dataframe
        """
        if isinstance(cols, str):
            cols = [cols]
        if isinstance(self._obj.columns, pd.MultiIndex):
            return self._obj.loc[:, (slice(None), cols)]
        else:
            return self._obj.loc[:, cols]
