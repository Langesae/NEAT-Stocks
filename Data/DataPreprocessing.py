'''
Pulling data from csv files on Github and compiling based on dates
Unable to pull directly from Github
Download the respository and give the glob functions the path to your files
    ending with *.csv
'''


import glob
import re
import csv

def preprocess():

    headerString = ''
    data_string = ''
    stockData = []
    allData = []
    count = 0
    stocks = ['AXP' , 'BAC' , 'BRK.B' , 'C' , 'CB', 'CME' , 'GS' , 'JPM' , 'USB', 'WFC']
    openCloseMetrics = ['DEMA', 'EMA', 'KAMA', 'MOM', 'RSI', 'SMA', 'TRIMA', 'WMA']
    timeIntervals = ['5', '10', '20', '40', '60', '121']

    # eight columns with headers
    dailyAdjusted = glob.glob('/Users/levimeyer/Desktop/NEAT-Stocks-master/Data/AlphaVantageCSV/DailyAdjusted/*.csv')

    # five columns with headers
    # ten stocks with 8 metrics
    # each metric has 6 time intervals
    openClose = glob.glob('/Users/levimeyer/Desktop/NEAT-Stocks-master/Data/AlphaVantageCSV/Open_Low_High_Close/*.csv')
    openClose.sort()

    # 4 metrics for each stock
    # each metric has 6 time intervals
    # each file has 2 columns (date, metric) except AROON
    # AROON has 3 columns (date, AROON up, AROON down)
    singleColumn = glob.glob('/Users/levimeyer/Desktop/NEAT-Stocks-master/Data/AlphaVantageCSV/SingleColumn/*.csv')
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

    return allData

    ##for i in range(0,10):
    ##    print(len(allData[i]))




'''
csv saving
    currently unavailable
'''

##fileName = 'test.csv'
##
##with open(fileName, 'a') as csvfile:
##    csvwriter = csv.writer(csvfile)
##    for g in allData:
##        csvwriter.writerow(g)
##
##csvfile.close()
##    
    

