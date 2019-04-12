README for DataPreprocessing.py

1. Download the GitHub repository or at least the 3 folders of data
2. Give each of the glob functions the path to the corresponding data files
3. IMPORTANT 
	I am returning all of the data
	running preprocess() on its own will cause allData to be printed
	use another file to save the object being returned by preprocess()
	running preprocess() should only take around 10-15 seconds max


The output is a list of lists. 
The outer list has a length of 10, each entry is the data for each stock
Each stock has 2013 entries (days of data), these are stored in a text string with the data preceding
Stocks are ordered alphabetically 
Data is stored based on how the files are read, but this is uniform for every stock
There are no headers because I don’t believe the network needs them since all data is ordered the same

allData[0][0]
	- this returns the day of data for the first stock
allData[0][1]
	- returns the second day of data for the first stock
allData[1][0]
	- returns the first dat of data for the second stock