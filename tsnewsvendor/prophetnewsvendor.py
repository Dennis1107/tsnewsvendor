import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import cross_validation
import plotly.express as px
from statistics import NormalDist


class ProphetNewsvendor:
    def __init__(self):
        pass
    def fit(**kwargs):
        """Calculate mean & standard deviation from cross validation results
        Args:
            **kwargs : facbook prophet cross_validation parameters 
        Returns:
            tuple: residual mean, residual standard deviation, residuals
        """
        df_cv = cross_validation(**kwargs)
        df_cv['Residuals'] = df_cv.yhat - df_cv.y
        mean_residual = df_cv.Residuals.mean()
        std_residual = df_cv.Residuals.std()
        return mean_residual, std_residual, df_cv.Residuals
    def plot_residuals(residuals:pd.Series):
        """Plot histogram of residuals.
        Note: Assumption of normal distributed residuals

        Args:
            residuals (pd.Series): previously calculated residuals
        """
        px.histogram(residuals).show()
    def applynewsvendor(mean:float, mean_res:float, std:float, price:float, cost:float):
        """calculate newsvendor quantity from forecast and previously calculated forecast error statistics
        Note: Assumption of normal distributed residuals

        Args:
            mean (float): forecast
            mean_res (float): mean error of forecast derived by cross_validation
            std (float): standard deviation of forecast derived by cross_validation
            price (float): sales price of item
            cost (float): variable cost of item

        Returns:
            float: newsvendor quantity
        """
        newsvendor_result = mean + mean_res + std * NormalDist().inv_cdf((price - cost) / price)
        return newsvendor_result
