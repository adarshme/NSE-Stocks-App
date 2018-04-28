# Leave a space between each Stock Symbol

import Stocks #Main API
import sys #To get Command Line arguments
import config #Config file API
import multiprocessing #It's obviuos :)

StartEndString = "------------------------------------" #For neat printing.

StockApp = Stocks.Stocks() #Initialize API
bcolors = Stocks.bcolors() #Initialize terminal colours
Config = config.Config() #Initialize Config file API

# Change this value to control the coloring in the terminal.
thresh = 2.5 #Doesn't matter for windows. (Atleast for now)

def SimpleGet(StocksList = sys.argv):
	#Check if argument passed or not and set start and end values accordingly.
	if StocksList == sys.argv:
		start = 2
		end = len(sys.argv)

	else:
		start = 0
		end = len(StocksList)

	#Loop each stock symbol from StocksList
	for i in range (start, end):
		try:
			Data = StockApp.ExtractStockPrice(StocksList[i])
			RequestComplete = True
		except Exception:
			#No internet, stock symbol which doesn't exist, etc.
			print ("Can't get", StocksList[i])
			print ()
			RequestComplete = False

		try:
			#Get values from API.
			lastPrice = StockApp.lastPrice
			pChange = StockApp.pChange
			change = StockApp.change
			lastUpdateTime = StockApp.lastUpdateTime
			companyName = StockApp.companyName

		except AttributeError:
			#Attribute error when above values do not exist.
			pass

		End = bcolors.ENDC #To close off ANSI codes.

		if RequestComplete:
			#Checks stock values and sets ANSI codes for clour, bold, etc.
			if float(pChange) > thresh:
				Start = bcolors.OKGREEN + bcolors.BOLD #Green and bold

			elif float(pChange) < -thresh:
				Start = bcolors.FAIL #Red

			elif float(pChange) < 0 and float(pChange) > -thresh:
				Start = bcolors.HEADER #Purple

			elif float(pChange) > 0 and float(pChange) < thresh:
				Start = bcolors.WARNING #Yellow

			else:
				Start = ""

			print (StartEndString) #For neat printing.
			print ("Stock:", Start, companyName, End)
			print ("Last Price:", bcolors.BOLD, lastPrice, End)
			print ("Percentage Change:", Start, pChange, End)
			print ("Absolute Change:", Start, change, End)
			print ("Last Updated Time:", lastUpdateTime)
			print ()

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

def MultiStockPrice(Stock, lock): #Lock needed for print lock or else printing gets messed up.
	try:
		Data = StockApp.ExtractStockPrice(Stock)
		RequestComplete = True
	except Exception:
		#No internet, stock symbol which doesn't exist, etc.
		print ("Can't get", Stock)
		print ()
		RequestComplete = False

	try:
		#Assign values
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

	lock.acquire() #Acquire print lock

	if RequestComplete:
		print (StartEndString)
		print ("Stock:", Start, companyName, End)
		print ("Last Price:", bcolors.BOLD, lastPrice, End)
		print ("Percentage Change:", Start, pChange, End)
		print ("Absolute Change:", Start, change, End)
		print ("Last Updated Time:", lastUpdateTime)
		print ()
		lock.release() #Release print lock

	else:
		lock.release() #Release print lock

def MultiGet(StocksList = sys.argv):
	lock = multiprocessing.Lock() #For print lock argument.
	#Check if argument passed or not and set start and end values accordingly.
	if StocksList == sys.argv:
		start = 2
		end = len(sys.argv)

	else:
		start = 0
		end = len(StocksList)

	Processes = [] #To store each process.

	for i in range (start, end):
		Processes.append (multiprocessing.Process(target = MultiStockPrice, args = (StocksList[i], lock, ))) #Create frocess for each stock symbol

	for i in Processes:
		i.start() #Start all processes

	for i in Processes:
		while i.is_alive(): #Standby till every processes is complete.
			pass

def ExecuteDefault():
	print (bcolors.OKBLUE + "No command found. Executing default: " + "get all-m" + bcolors.ENDC)
	MultiGet(Config.GetAllStockSymbols()) #Execute default command.

if __name__ == "__main__": #Absolutely needed for windows.
	if len(sys.argv) > 1: #If some command has been given.
		if sys.argv[1] == "get":
			try:
				if sys.argv[2] == "all-m": #Multiprocessing
					MultiGet(Config.GetAllStockSymbols())

				elif sys.argv[2] == "all": #Sequential
					SimpleGet(Config.GetAllStockSymbols())

				else:
					SimpleGet() #Default

			except IndexError:
				print ()

		elif sys.argv[1] == "add":
			for i in range (2, len(sys.argv)):
				Config.AddStockSymbol(sys.argv[i])

		elif sys.argv[1] == "remove":
			for i in range (2, len(sys.argv)):
				Config.RemoveStockSymbol(sys.argv[i])

		elif sys.argv[1] == "status":
			print ("Following stock symbols have been added:-")
			for i in Config.GetAllStockSymbols():
				print (" ", i) #Neat printing

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
		     Use `get all-m` to get faster results, but stocks are shown randomly.

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

		else:
			#Wrong command
			print (bcolors.OKBLUE + "I don't know that command!" + bcolors.ENDC)

	else:
		#If no command passed
		ExecuteDefault()

	print (StartEndString) #Prints right at the end of program.