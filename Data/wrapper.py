import stockprediction as prediction
import os
import csv
import pandas as pd
import xlrd

stock = ''
stocks = ['AXP', 'BAC', 'BRK.B', 'CB', 'C', 'CME', 'GS', 'JPM', 'USB', 'WFC']
buyPre = 5
sellPre = 5
percentage = 0 
buy = False
sell = False
hold = False
FileName = os.getcwd()

def calc (file, buyPre, sellPre, buy , sell, hold):
	with open(file) as f:
		reader = csv.reader(f)
		a = list(reader)
		prediction = float(a[-1][-1])
		actual = float(a[-1][-2])
		difference = prediction - actual
		percentage = (difference / actual) * 100
		if percentage >= buyPre:
			buy = True
		elif percentage <= (sellPre * -1):
			sell = True
		else:
			hold = True
		return percentage, buy, sell, hold
		

while True:
	use = input("Do you want to run the network. Y/N? ")
	if use == 'Y':
		buyPre = int(input("What is the percentage of gain for a buy? "))
		sellPre = int(input("What is the percentage of loss for a sell? "))
		print("Plug in Laptop network could overload internal battery")
		print(stocks)
		stock = input("What stock above would you like to use? ")
		while stock not in stocks:
			print("Not in list. Try again. ")
			stock = input("What stock above would you like to use? ")
		prediction.main(stock)
		FileName += '/Results/' + stock + '_Optimizer_Initializer_CostFunction_FinalPredictions.csv' 
		percentage, buy, sell, hold = (calc(FileName, buyPre, sellPre, buy, sell, hold))
		if sell == True:
			print("We advise you to sell " + stock + ".")
		elif buy == True:
			print("We advise you to buy " + stock + ".")
		elif hold == True:
			print("We advise you to hold " + stock + ".")
	elif use == 'N':
		break
		

