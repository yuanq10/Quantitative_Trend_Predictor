from stockstats import StockDataFrame
import pandas as pd

def compute_cci(historical_data, analysis_start_date):
    analysis_start_date = pd.to_datetime(analysis_start_date)
    stock = StockDataFrame.retype(historical_data.copy())
    stock.index = stock.index.tz_localize(None)

    cci = stock['cci_20']

    # TRIM WARM-UP PERIOD
    cci = cci.loc[analysis_start_date:]
    return cci