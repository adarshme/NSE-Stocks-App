# Run this program to get all your stocks info at once.

import sys
import collections
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import config

Config = config.Config()

class Stocks():
	def __init__(self):
		self.LoadStocks ()

	def LoadStocks (self):
		self.StockSymbols = collections.OrderedDict()

		# Add/Remove your Stocks here
		# Keys are names of the stocks, values are the Stock Symbols
		# 2 examples have been given
		self.StockSymbols.update({"Reliance Industries Limited" : "RELIANCE",
			"Infosys Limited" : "INFY"})

		self.StockSymbols = collections.OrderedDict(sorted(self.StockSymbols.items(), key=lambda t: t[0]))
		
	def PrintAll(self):
		# Change this value to control the coloring in the terminal.
		thresh = 2.5
		for Stock in self.StockSymbols:
			try:
				AllData = self.ExtractStockPrice (self.StockSymbols[Stock])

				if float(self.pChange) > 0 and float(self.pChange) < thresh:
					print (bcolors.WARNING + " " + str(self.StockSymbols[Stock] + " "*(10 - len (self.StockSymbols[Stock])) + " :" + " " + AllData) + bcolors.ENDC)

				elif float(self.pChange) > thresh:
					print (bcolors.OKGREEN + bcolors.BOLD + " " + str(self.StockSymbols[Stock] + " "*(10 - len (self.StockSymbols[Stock])) + " :" + " " + AllData) + bcolors.ENDC)

				elif float(self.pChange) < 0 and float(self.pChange) > -thresh:
					print (bcolors.HEADER + " " + str(self.StockSymbols[Stock] + " "*(10 - len (self.StockSymbols[Stock])) + " :" + " " + AllData) + bcolors.ENDC)

				elif float(self.pChange) < -thresh:
					print (bcolors.FAIL + " " + str(self.StockSymbols[Stock] + " "*(10 - len (self.StockSymbols[Stock])) + " :" + " " + AllData) + bcolors.ENDC)

				else:
					print (" " + str(self.StockSymbols[Stock] + " "*(10 - len (self.StockSymbols[Stock])) + " :" + " " + AllData))

			except Exception:
				print ("Can't get {}".format (self.StockSymbols[Stock]), " "*(61 - len ("Can't get {}".format (self.StockSymbols[Stock]))))

			print ()

	def UrlBuilder(self, StockSymbol):
		self.BaseUrl = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="

		self.FinalUrl = self.BaseUrl + StockSymbol

		return (self.FinalUrl)

	def ExtractStockPrice(self, StockSymbol):
		Url = self.UrlBuilder (StockSymbol)

		if Url != None:
			hdr = {'User-Agent': 'Mozilla/5.0'}

			req = Request(Url ,headers=hdr)

			page = urlopen(req)

			try:
				soup = BeautifulSoup(page, Config.GetAllSettings()["parser"])
			except Exception as e:
				print ("Parser in settings not installed. Using default parser.")
				soup = BeautifulSoup(page, "html.parser")				

			JumbledInfo = str(soup.find("div", {"id": "responseDiv"}))

			JumbledInfo = JumbledInfo[JumbledInfo.index("{"):][::-1]

			JumbledInfo = JumbledInfo[JumbledInfo.index("}"):][::-1]

			InfoDict = json.loads (JumbledInfo)

			MainInfoDict = InfoDict["data"][0]

			self.lastPrice = MainInfoDict["lastPrice"]
			self.pChange = MainInfoDict["pChange"]
			self.change = MainInfoDict["change"]
			self.companyName = MainInfoDict["companyName"]

			self.lastUpdateTime = InfoDict["lastUpdateTime"]


			return str(" "*(8 - len(self.lastPrice)) + self.lastPrice + "; " + " "*(5 - len(self.pChange)) + self.pChange + "; " + " "*(6 - len(self.change)) + self.change + ";    " + self.lastUpdateTime)

class bcolors:
	if sys.platform in "win32 cygwin":
		LBLUE = ''
		HEADER = ''
		OKBLUE = ''
		OKGREEN = ''
		WARNING = ''
		FAIL = ''
		DWARNING = ''
		ENDC = ''
		BOLD = ''
		UNDERLINE = ''

	else:
		LBLUE = '\033[96m'
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		DWARNING = '\033[90m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

if __name__ == '__main__':
	StartEndString = "------------------------------------"
	TableHeading = "StckSymb     StckPrice  %Chng  Abs.Chng        LstUpTime"

	StocksApp = Stocks()
	print (StartEndString)
	print (TableHeading)
	StocksApp.PrintAll()
	print (StartEndString)