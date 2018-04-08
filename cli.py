# Type "python cli-search.py STOCKSYMBOLS" in the terminal.
# Example - "python cli-search.py reliance infy"
# Leave a space between each Stock Symbol
# If you're in a system where python2 is default-
# Change "python" to "python3"

import Stocks
import sys

StartEndString = "------------------------------------"

StockApp = Stocks.Stocks()
bcolors = Stocks.bcolors()

# Change this value to control the coloring in the terminal.
thresh = 2.5

for i in range (1, len(sys.argv)):
	try:
		Data = StockApp.ExtractStockPrice(sys.argv[i])
		RequestComplete = True
	except Exception as e:
		print ("Can't get", sys.argv[i])
		print ()
		RequestComplete = False

	try:
		lastPrice = StockApp.lastPrice
		pChange = StockApp.pChange
		change = StockApp.change
		lastUpdateTime = StockApp.lastUpdateTime
		companyName = StockApp.companyName

	except AttributeError:
		pass

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
