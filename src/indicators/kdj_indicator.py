from stockstats import StockDataFrame
import pandas as pd

def compute_kdj(historical_data, analysis_start_date):
    analysis_start_date = pd.to_datetime(analysis_start_date)
    stock = StockDataFrame.retype(historical_data.copy())
    stock.index = stock.index.tz_localize(None)

    kdj_k = stock['kdjk']
    kdj_d = stock['kdjd']
    kdj_j = stock['kdjj']
    #print(kdj)

    # TRIM WARM-UP PERIOD
    kdj_k = kdj_k.loc[analysis_start_date:]
    kdj_d = kdj_d.loc[analysis_start_date:]
    kdj_j = kdj_j.loc[analysis_start_date:]
    return kdj_k, kdj_d, kdj_j