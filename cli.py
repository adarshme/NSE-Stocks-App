# Leave a space between each Stock Symbol

import Stocks
import sys
import config
import multiprocessing

StartEndString = "------------------------------------"

StockApp = Stocks.Stocks()
if sys.platform in "win32 cygwin":
	bcolors = Stocks.nocolors()
else:
	bcolors = Stocks.bcolors()
Config = config.Config()

# Change this value to control the coloring in the terminal.
thresh = 2.5

def SimpleGet(StocksList = sys.argv):
	if StocksList == sys.argv:
		start = 2
		end = len(sys.argv)

	else:
		start = 0
		end = len(StocksList)

	for i in range (start, end):
		try:
			Data = StockApp.ExtractStockPrice(StocksList[i])
			RequestComplete = True
		except Exception as e:
			print ("Can't get", StocksList[i])
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

def MultiStockPrice(Stock, lock):
	try:
		Data = StockApp.ExtractStockPrice(Stock)
		RequestComplete = True
	except Exception as e:
		print ("Can't get", Stock)
		print ()
		RequestComplete = False

	try:
		lastPrice = StockApp.lastPrice
		pChange = StockApp.pChange
		change = StockApp.change
		lastUpdateTime = StockApp.lastUpdateTime
		companyName = StockApp.companyName

	except AttributeError:
		print ("AttributeError")

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

	lock.acquire()

	if RequestComplete:
		print (StartEndString)
		print ("Stock:", Start, companyName, End)
		print ("Last Price:", bcolors.BOLD, lastPrice, End)
		print ("Percentage Change:", Start, pChange, End)
		print ("Absolute Change:", Start, change, End)
		print ("Last Updated Time:", lastUpdateTime)
		print ()
		lock.release()

	else:
		lock.release()

	return True

def MultiGet(StocksList = sys.argv):
	lock = multiprocessing.Lock()
	if StocksList == sys.argv:
		start = 2
		end = len(sys.argv)

	else:
		start = 0
		end = len(StocksList)

	Processes = []

	for i in range (start, end):
		Processes.append (multiprocessing.Process(target = MultiStockPrice, args = (StocksList[i], lock, )))

	for i in Processes:
		i.start()

	for i in Processes:
		while i.is_alive():
			pass

if sys.argv[1] == "get":
	if sys.argv[2] == "all-m":
		MultiGet(Config.GetAllStockSymbols())

	elif sys.argv[2] == "all":
		SimpleGet(Config.GetAllStockSymbols())

	else:
		SimpleGet()

elif sys.argv[1] == "add":
	for i in range (2, len(sys.argv)):
		Config.AddStockSymbol(sys.argv[i])

elif sys.argv[1] == "remove":
	for i in range (2, len(sys.argv)):
		Config.RemoveStockSymbol(sys.argv[i])

elif sys.argv[1] == "status":
	print ("Following stock symbols have been added:-")
	for i in Config.GetAllStockSymbols():
		print (" ", i)

elif sys.argv[1] == "help":
	message = '''
 List of commands available: -
   1) get all
   2) get
   3) add
   4) remove
   5) status

   1) get all:-
     Use 'get all' to show all your stock values.

   2) get:-
     Use 'get STOCKSYMBOLS' to get the values of particular stocks.

   3) add:-
     Use 'add STOCKSYMBOLS' to add stocks to the list of all your stocks.

   4) remove:-
     Use 'remove STOCKSYMBOLS' to remove stocks from your list of stocks.

   5) status:-
     Use 'status' to see your list of stocks

 Wherever STOCKSYMBOLS have been used, it means you can use a single stock symbol or multiple stock symbols seperated by spaces

 To call a command, type:-
   python cli.py COMMAND

 if you are in a system which has python2 by default, type:-
   python3 cli.py COMMAND'''

	print (message)

print (StartEndString)