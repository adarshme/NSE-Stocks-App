import os
import configparser
import Stocks
import urllib.error

StockApp = Stocks.Stocks()

class Config():
	def __init__(self):
		self.config = configparser.ConfigParser()

		self.LoadConfigFile()

		if self.File == []:
			self.config["Stocks"] = {}
			self.WriteFile()

			self.LoadConfigFile()

	def AddStockSymbol(self, StockSymbol):
		try:
			Data = StockApp.ExtractStockPrice(StockSymbol.lower())
		except IndexError:
			Data = None
		except urllib.error.HTTPError:
			Data = None

		if StockSymbol in self.GetAllStockSymbols():
			print (StockSymbol.lower(), "has already been added")
			Data = False

		if Data:
			self.config["Stocks"][StockSymbol] = StockApp.companyName

			self.WriteFile()

			print ("Added", StockApp.companyName)

		elif Data == None:
			print ("Couln't find", StockSymbol.lower())

	def RemoveStockSymbol(self, StockSymbol):
		if self.config.has_option("Stocks", StockSymbol):
			self.config.remove_option("Stocks", StockSymbol)
			RemoveSuccessful = True

		else:
			print (StockSymbol.lower(), "is not in your list")
			RemoveSuccessful = False

		self.WriteFile()
		if RemoveSuccessful:
			print ("Removed", StockSymbol.lower())
		return True

	def WriteFile(self):
		with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'), 'w') as configfile:
			self.config.write (configfile)

		self.LoadConfigFile()

	def LoadConfigFile(self):
		self.File = self.config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

	def GetAllStockSymbols(self):
		StockSymbols = [i for i in self.config.options("Stocks")]

		return StockSymbols