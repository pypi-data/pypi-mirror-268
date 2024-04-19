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
import math

import pandas as pd

import financefunctions.functions

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
@pd.api.extensions.register_series_accessor("ff")
class FinanceFunctionsSeries:
    def __init__(self, pandas_obj: pd.Series) -> None:
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj) -> None | RuntimeError:
        if not isinstance(obj, pd.Series):
            raise RuntimeError(f"expected pandas series object, received {type(obj)}")

    # -------------------------------------------------------------
    # Values, StandardDeviations and Means
    # -------------------------------------------------------------
    def vals_p(self, dropna: bool = False) -> pd.Series:
        """return positive values of series

        Parameters
        ----------
        dropna : bool, optional
            drop Nan values, by default False

        Returns
        -------
        pandas dataframe
            pandas series with positive values
        """
        return self._obj[self._obj > 0].dropna() if dropna else self._obj[self._obj > 0]

    def vals_n(self, dropna: bool = False) -> pd.Series:
        """return negative values of series

        Parameters
        ----------
        dropna : bool, optional
            drop Nan values, by default False

        Returns
        -------
        pandas dataframe
            pandas series with positive values
        """
        return self._obj[self._obj < 0].dropna() if dropna else self._obj[self._obj < 0]

    def std_p(self, ddof: int = 1) -> float:
        """standard deviation of positive values

        Parameters
        ----------
        ddof : int, optional
            delta degrees of freedom, by default 1 ( standard param from used std-function )

        Returns
        -------
        float
            float with standard deviations of positive values
        """
        return self._obj[self._obj > 0].std(ddof=ddof)

    def std_n(self, ddof: int = 1) -> float:
        """standard deviation of negative values

        Parameters
        ----------
        ddof : int, optional
            delta degrees of freedom, by default 1 ( standard param from used std-function )

        Returns
        -------
        float
            float with standard deviations of negative values
        """
        return self._obj[self._obj < 0].std(ddof=ddof)

    def mean_p(self) -> float:
        """mean of positive values

        Returns
        -------
        float
            float with mean of positive values
        """
        return self._obj[self._obj > 0].mean()

    def mean_n(self) -> float:
        """mean of negative values

        Returns
        -------
        float
            float with mean of negative values
        """
        return self._obj[self._obj < 0].mean()

    # -------------------------------------------------------------
    # Normalize function
    # -------------------------------------------------------------
    def norm(self) -> pd.Series:
        """normalize series to first line

        Returns
        -------
        pandas series
            normalized series to first line
        """
        return self._obj.div(self._obj.iloc[0]).mul(100)

    # -------------------------------------------------------------
    # CAGR function
    # -------------------------------------------------------------
    def cagr(self) -> float:
        """calculate cagr (compound annual growth rate) of a series.

        Returns
        -------
        float
            float with cagr
        """
        df = self._obj.to_frame()
        df["return"] = df[self._obj.name].pct_change()
        df.dropna(inplace=True)
        cumulative_return = (1 + df["return"]).cumprod().iloc[-1]
        start_date, end_date = df.index[0], df.index[-1]
        period_years = (end_date - start_date).days / 365.25
        return cumulative_return ** (1 / period_years) - 1

    # -------------------------------------------------------------
    # volatility function
    # -------------------------------------------------------------
    def volatility(self) -> float:
        """calculate volatility of a series.

        Returns
        -------
        float
            float with volatility
        """
        df = self._obj.to_frame()
        df["return"] = df[self._obj.name].pct_change()
        period_years = (self._obj.index[-1] - self._obj.index[0]).days / 365.25
        ratio_to_annual = df["return"].count() / period_years
        vol = df["return"].std() * math.sqrt(ratio_to_annual)
        return vol

    # -------------------------------------------------------------
    # sharpe ratio function
    # -------------------------------------------------------------
    def sharp_ratio(self, risk_free_rate: float = 0.03) -> float:
        """calculate sharpe ratio of a series.

        Parameters
        ----------
        risk_free_rate : float, optional
            risk free rate, by default 0.03

        Returns
        -------
        float
            float with volatility
        """
        return (self.cagr() - risk_free_rate) / self.volatility()

    # -------------------------------------------------------------
    # momentum value
    # -------------------------------------------------------------
    def momentum(self, period: int = 90) -> pd.Series:
        """calculate momentum of the series with exponential regression.

        Parameters
        ----------
        period : int, optional
            period to calculate momentum, by default 90

        Returns
        -------
        pandas series
            momentum values for complete series
        """
        return self._obj.rolling(window=period).apply(financefunctions.functions.momentum_value)
