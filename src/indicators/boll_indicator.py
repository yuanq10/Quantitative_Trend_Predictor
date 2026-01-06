from stockstats import StockDataFrame
import pandas as pd

def compute_boll(historical_data, analysis_start_date):
    analysis_start_date = pd.to_datetime(analysis_start_date)
    stock = StockDataFrame.retype(historical_data.copy())
    stock.index = stock.index.tz_localize(None)

    close = stock['close']
    boll_mid = stock['boll']
    boll_up = stock['boll_ub']
    boll_low = stock['boll_lb']
    #print(boll)

    # TRIM WARM-UP PERIOD
    close = close.loc[analysis_start_date:]
    boll_mid = boll_mid.loc[analysis_start_date:]
    boll_up = boll_up.loc[analysis_start_date:]
    boll_low = boll_low.loc[analysis_start_date:]
    return close, boll_mid, boll_up, boll_low