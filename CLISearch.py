# Type "python CLISearch.py STOCKSYMBOL" in the terminal.
# If you're in a system where python2 is default-
# Type "python3 CLISearch.py STOCKSYMBOL"

import Stocks
import sys

StartEndString = "------------------------------------"

StockApp = Stocks.Stocks()
bcolors = Stocks.bcolors()

# Change this value to control the coloring in the terminal.
thresh = 2.5

Data = StockApp.ExtractStockPrice(sys.argv[1])

RequestComplete = False

try:
	lastPrice = StockApp.lastPrice
	pChange = StockApp.pChange
	change = StockApp.change
	lastUpdateTime = StockApp.lastUpdateTime
	companyName = StockApp.companyName

	RequestComplete = True

except AttributeError:
	print ("Could not find", sys.argv[1])

End = bcolors.ENDC

if RequestComplete:
	if float(pChange) > thresh:
		Start = bcolors.OKGREEN + bcolors.BOLD

	elif float(pChange) < -thresh:
		Start = bcolors.FAIL

	elif float(pChange) < 0 and float(pChange) > -thresh:
		Start = bcolors.HEADER

	elif float(pChange) > 0 and float(pChange) < thresh:
		Start = bcolors.WARNING

	else:
		Start = ""

'''
print (StartEndString)
print ()
print (Start, "Stock:", companyName, End)
print (Start, "Last Price:", lastPrice, End)
print (Start, "Percentage Change:", pChange, End)
print (Start, "Absolute Change:", change, End)
print (Start, "Last Updated Time:", lastUpdateTime, End)
print ()
print (StartEndString)'''

if RequestComplete:
	print (StartEndString)
	print ("Stock:", Start, companyName, End)
	print ("Last Price:", bcolors.BOLD, lastPrice, End)
	print ("Percentage Change:", Start, pChange, End)
	print ("Absolute Change:", Start, change, End)
	print ("Last Updated Time:", lastUpdateTime)
	print ()
	print (StartEndString)