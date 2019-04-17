'''
Pulling data from csv files on Github and compiling based on dates
Unable to pull directly from Github
Download the respository and give the glob functions the path to your files
    ending with *.csv
'''


import glob
import re
import csv
import pandas
import os
import numpy


def preprocess(desiredStock, type):
    headerString = ''
    data_string = ''
    stockData = []
    allData = []
    count = 0
    stocks = ['AXP' , 'BAC' , 'BRK.B' , 'C' , 'CB', 'CME' , 'GS' , 'JPM' , 'USB', 'WFC']
    openCloseMetrics = ['DEMA', 'EMA', 'KAMA', 'MOM', 'RSI', 'SMA', 'TRIMA', 'WMA']
    timeIntervals = ['5', '10', '20', '40', '60', '121']

    # eight columns with headers
    dailyAdjusted = glob.glob('C:/Users/BabyHulk/Documents/GitHub/NEAT-Stocks/Data/' + str(type) + '/DailyAdjusted/*.csv')

    # five columns with headers
    # ten stocks with 8 metrics
    # each metric has 6 time intervals
    openClose = glob.glob('C:/Users/BabyHulk/Documents/GitHub/NEAT-Stocks/Data/' + str(type) + '/Open_Low_High_Close/*.csv')
    openClose.sort()

    # 4 metrics for each stock
    # each metric has 6 time intervals
    # each file has 2 columns (date, metric) except AROON
    # AROON has 3 columns (date, AROON up, AROON down)
    singleColumn = glob.glob('C:/Users/BabyHulk/Documents/GitHub/NEAT-Stocks/Data/' + str(type) + '/SingleColumn/*.csv')
    singleColumn.sort()


    allFiles = dailyAdjusted + openClose + singleColumn

    stockCount = 0

    for stock in stocks:
        for i in allFiles:
            if stock in i:
                g = open(i, 'r')
                header = g.readline()
                for dataLine in g:
                    if stockCount == 0:
                        dataLine = dataLine[:(len(dataLine) - 1)]
                        stockData.append(dataLine)
                    else:
                        dataLine = dataLine[11:(len(dataLine) - 1)]
                        stockData[count] = str(stockData[count]) + ',' + dataLine
                    count += 1
                count = 0
                stockCount += 1
        stockCount = 0
        allData.append(stockData)
        stockData = []

    index = stocks.index(desiredStock)

    dataFrame = makeDataFrame(allData, index)

    dataFrame = dataFrame.drop([0] , axis = 1)

    dataFrame = dataFrame.values

    return dataFrame



'''
Turning allData into a data frame
Outputs data for one stock in data frame
'''




def makeDataFrame(data, index):

    count = 0
    
    stock = data[index]
    for day in range(0,len(stock)):
        if count == 0:
            dataFrame = pandas.DataFrame(stock[day].split(','))
        else:
            df2 = pandas.DataFrame(stock[day].split(','))
            dataFrame = pandas.concat([dataFrame,df2], axis = 1)
        count += 1


    return dataFrame.transpose()


def preprocessAndSave(preprocessDataFrame, name):
    cwd = os.getcwd()
    path = cwd + '/' + name + '.csv'
    numpy.savetxt(path, preprocessDataFrame, delimiter=",")
    return

if __name__ == '__main__':
    APXData = preprocess('AXP', 'TrainData')
    preprocessAndSave(APXData, 'APXTest')










'''
csv saving
    currently unavailable
'''


    



