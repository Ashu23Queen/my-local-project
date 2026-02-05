from pytrends.request import TrendReq
import pandas as pd

def get_trend_data(keyword_list):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keyword_list, cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time()
    if not data.empty:
        data = data.drop(columns=['isPartial'])
    return data