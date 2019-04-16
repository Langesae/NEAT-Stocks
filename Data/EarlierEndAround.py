from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import time
import pandas

symbol_list = ['BRK.B', 'JPM', 'BAC', 'WFC', 'C', 'USB', 'AXP', 'GS', 'CME', 'CB']
series_list = ['SMA', 'EMA', 'WMA', 'DEMA', 'TRIMA', 'KAMA', 'RSI', 'MOM']
series_no_price_list = ['CCI', 'WillR', 'ADX', 'AROON']
time_period_list = [5, 10, 20, 40, 60, 121]
price_type_list = ['open', 'low', 'high', 'close']
interval = 'daily'
Start_Date = '2018-01-02'
End_Date = '2019-03-31'


def Master_Symbol_Loop(dict_kwargs, symbol_list, series_list, time_period_list, price_type_list, start_date, end_date):
    dict_kwargs['interval'] = interval
    for symbol in symbol_list:
        dict_kwargs['symbol'] = symbol
        Series_Loop(dict_kwargs, series_list, time_period_list, price_type_list, start_date, end_date)


def Series_Loop(dict_kwargs, series_list, time_period_list, price_type_list, start_date, end_date):
    for series in series_list:
        Time_Period_Loop(dict_kwargs, series, time_period_list, price_type_list, start_date, end_date)


def Time_Period_Loop(dict_kwargs, series, time_period_list, price_type_list, start_date, end_date):
    for time_period in time_period_list:
        dict_kwargs['time_period'] = time_period
        Standard_TechIndicator(dict_kwargs, series, price_type_list, start_date, end_date)


def Standard_TechIndicator(dict_kwargs, series, price_type_list, start_date, end_date):
    starttime = time.time()
    ti = TechIndicators(key='6RX0I0CC3SZBVUCI', output_format='pandas')
    appended_data = []
    function = ('get_' + series.casefold())
    if price_type_list == []:
        data, meta_data = getattr(ti, function)(**dict_kwargs)
        file_name = 'C:\\Users\\BabyHulk\\PycharmProjects\\IntelligentTrader\\AlphaVantageCSV\\TestData\\SingleColumn' \
                    + '\\' + dict_kwargs['symbol'] + '_' + series + '_' + str(dict_kwargs['time_period']) \
                    + '.csv'
        appended_data_slice = data.loc[start_date:end_date]
        appended_data_slice.to_csv(file_name)
        time.sleep(3.0 - ((time.time() - starttime) % 3.0))
    else:
        for price in price_type_list:

            columns_name = {series: price}

            data, meta_data = getattr(ti, function)(**dict_kwargs)
            data.rename(columns=columns_name, inplace=True)
            appended_data.append(data)

        file_name = 'C:\\Users\\BabyHulk\\PycharmProjects\\IntelligentTrader\\AlphaVantageCSV\\TestData\\Open_Low_High_Close\\' \
                    + dict_kwargs['symbol'] + '_' + series + '_' + str(dict_kwargs['time_period']) + '.csv'

        appended_data = pandas.concat(appended_data, axis=1)
        appended_data_slice = appended_data.loc[start_date:end_date]
        appended_data_slice.to_csv(file_name)
        time.sleep(15.0 - ((time.time() - starttime) % 15.0))

def Daily_Adjusted_Loop(dict_kwargs, symbol_list, start_date, end_date):
    for symbol in symbol_list:
        dict_kwargs['symbol'] = symbol
        Time_Series_Loop(dict_kwargs, start_date, end_date)

def Time_Series_Loop(dict_kwargs, start_date, end_date):
    starttime = time.time()
    ts = TimeSeries(key='6RX0I0CC3SZBVUCI', output_format='pandas')
    function = 'get_daily_adjusted'
    data, meta_data = getattr(ts, function)(**dict_kwargs)
    file_name = 'C:\\Users\\BabyHulk\\PycharmProjects\\IntelligentTrader\\AlphaVantageCSV\\TestData\\DailyAdjusted' \
                + '\\' + dict_kwargs['symbol'] + '_' + 'DailyAdjusted' + '.csv'
    data_slice = data.loc[start_date:end_date]
    data_slice.to_csv(file_name)
    time.sleep(3.0 - ((time.time() - starttime) % 3.0))




Master_Symbol_Loop({}, symbol_list, series_list, time_period_list, price_type_list, Start_Date, End_Date)

"This is the no_price_list series of functions. The [] for the price list is a end around."
Master_Symbol_Loop({}, symbol_list, series_no_price_list, time_period_list, [], Start_Date, End_Date)

Daily_Adjusted_Loop({'outputsize' : 'full'}, symbol_list, Start_Date, End_Date)
