import os # For os.path to get complete config file dir.
import configparser # Make and manage config files
import Stocks # Main API
import urllib.error # To make an exception when no internet and other http error

class Config():
	def __init__(self):
		self.config = configparser.ConfigParser() # Init

		self.LoadConfigFile()

		if self.File == []:
			self.config["Stocks"] = {}
			self.WriteFile()

		self.FillSettings()

		self.LoadConfigFile()

	def FillSettings(self):
		if not self.config.has_section("Settings"):
			self.config["Settings"] ={}

		if not self.config.has_option("Settings", "parser"):
			self.config["Settings"]["parser"] = "html.parser"

		if not self.config.has_option("Settings", "default"):
			self.config["Settings"]["default"] = "get all-m"

		self.WriteFile()

	def AddStockSymbol(self, StockSymbol):
		StockApp = Stocks.Stocks()
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

	def GetAllSettings(self):
		Settings ={}
		for i in self.config["Settings"]:
			Settings[i] = self.config.get("Settings", i)

		return Settings