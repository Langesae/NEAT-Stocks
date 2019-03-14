from alpha_vantage.techindicators import TechIndicators
import time
import pandas

symbol_list = ['BRK.B', 'JPM', 'BAC', 'WFC', 'C', 'USB', 'AXP', 'GS', 'CME', 'CB']
series_list = ['SMA', 'EMA', 'WMA', 'DEMA', 'TRIMA', 'KAMA', 'RSI', 'MOM']
series_no_price_list = ['CCI', 'WillR', 'ADX', 'AROON']
time_period_list = [5, 10, 20, 40, 60, 121]
price_type_list = ['open', 'low', 'high', 'close']
interval = 'daily'
Start_Date = '2010-01-04'
End_Date = '2017-12-29'



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
        file_name = 'C:\\Users\\BabyHulk\\PycharmProjects\\IntelligentTrader\\AlphaVantageCSV\\SingleColumn' \
                    + '\\' + dict_kwargs['symbol'] + '_' + series + '_' + str(dict_kwargs['time_period']) \
                    + '.csv'
        appended_data_slice = data.loc[start_date:end_date]
        appended_data_slice.to_csv(file_name)
        time.sleep(3.0 - ((time.time() - starttime) % 3.0))
    else:
        for price in price_type_list:
            function_kwargs_dict = {"symbol": symbol, "interval": interval,
                                    "time_period": time_period, "series_type": price}
            columns_name = {series: price}

            data, meta_data = getattr(ti, function)(**function_kwargs_dict)
            data.rename(columns=columns_name, inplace=True)
            appended_data.append(data)

        file_name = 'C:\\Users\\BabyHulk\\PycharmProjects\\IntelligentTrader\\AlphaVantageCSV' + '\\' \
                    + symbol + '_' + series + '_' + str(time_period) + '.csv'

        appended_data = pandas.concat(appended_data, axis=1)
        appended_data_slice = appended_data.loc[start_date:end_date]
        appended_data_slice.to_csv(file_name)
        time.sleep(15.0 - ((time.time() - starttime) % 15.0))



#Master_Symbol_Loop({}, symbol_list, series_no_price_list, time_period_list, price_type_list, interval, Start_Date, End_Date)

"This is the no_price_list series of functions. The [] for the price list is a backend."
Master_Symbol_Loop({}, symbol_list, series_no_price_list, time_period_list, [], Start_Date, End_Date)


"BollingBands"
#Master_Symbol_Loop({'matype':'EMA'}, ['BBANDS'], time_period_list, [], interval, Start_Date, End_Date)


#Standard_TechIndicator('WFC', 'AROON', 10, [], interval, Start_Date, End_Date)
#Time_Period_Loop('C', 'WILLR', time_period_list, [], interval, Start_Date, End_Date)

#Standard_TechIndicator('WFC', 'SMA', 5, price_type_list, interval, Start_Date, End_Date)
#Standard_TechIndicator('BRK.b', 'EMA', 20, price_type_list, interval, Start_Date, End_Date)
#Standard_TechIndicator('BRK.b', 'EMA', 40, price_type_list, interval, Start_Date, End_Date)
#Standard_TechIndicator('BRK.b', 'EMA', 60, price_type_list, interval, Start_Date, End_Date)
#Standard_TechIndicator('BRK.b', 'EMA', 121, price_type_list, interval, Start_Date, End_Date)