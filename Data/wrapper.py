import stockprediction as prediction
import os

days = 1
stock = ''
save = False
plot = True
stocks = ['AXP', 'BAC', 'BRK.B', 'CB', 'C', 'CME', 'GS', 'JPM', 'USB', 'WFC']
buy = 5
sell = 5
FileName = os.getcwd()

while True:
	use = input("Do you want to run the network. Y/N? ")
	if use == 'Y':
		buy = input("What is the percentage of gain for a buy? ")
		buy = input("What is the percentage of loss for a sell? ")
		print("Plug in Laptop network could overload internal battery")
		print(stocks)
		stock = input("What stock above would you like to use? ")
		while stock not in stocks:
			print("Not in list. Try again. ")
			stock = input("What stock above would you like to use? ")
		prediction.main(stock)
		FileName += '/Results/' + stock + '-Prediction_vs_Actual'
	elif use == 'N':
		break
		
		
		


	
	
