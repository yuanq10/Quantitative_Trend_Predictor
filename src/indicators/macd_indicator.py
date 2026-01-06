from stockstats import StockDataFrame
import pandas as pd

def compute_macd(historical_data, analysis_start_date):
    """
    Compute MACD using warm-up data and return trimmed analysis period only.

    Parameters
    ----------
    historical_data : DataFrame
        Data including warm-up + analysis period
    analysis_start_date : str or datetime
        Start date of analysis period

    Returns
    -------
    macd : Series
    macd_signal : Series
    macd_histogram : Series
    """
    analysis_start_date = pd.to_datetime(analysis_start_date)
    stock = StockDataFrame.retype(historical_data.copy())
    stock.index = stock.index.tz_localize(None)

    macd = stock['macd_5,11,4']
    macd_signal = stock['macds_5,11,4']
    macd_histogram = stock['macdh_5,11,4']
    #print(macd)

    # TRIM WARM-UP PERIOD
    macd = macd.loc[analysis_start_date:]
    macd_signal = macd_signal.loc[analysis_start_date:]
    macd_histogram = macd_histogram.loc[analysis_start_date:]

    return macd, macd_signal, macd_histogram