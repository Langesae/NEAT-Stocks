import stockpredictionTest as prediction


# input vars
days = 1
stock = ''
save = False
plot = True
stocks = ['AXP', 'BAC', 'BRK.B', 'CB', 'C', 'CME', 'GS', 'JPM', 'USB', 'WFC']

while True:
	use = input("Do you want to run the network. Y/N? ")
	if use == 'Y':
		print("Plug in Laptop network could overload internal battery")
		print(stocks)
		stock = input("What stock above would you like to use? ")
		while stock not in stocks:
			print("Not in list. Try again. ")
			stock = input("What stock above would you like to use? ")
		prediction.main(stock)
	