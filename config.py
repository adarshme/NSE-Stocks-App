import configparser
import Stocks

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
			Data = StockApp.ExtractStockPrice(StockSymbol)
		except IndexError:
			Data = None

		if Data:
			self.config["Stocks"][StockSymbol] = StockApp.companyName

			self.WriteFile()

			print ("Added", StockApp.companyName)

		else:
			print ("Couln't find", StockSymbol)

	def RemoveStockSymbol(self, StockSymbol):
		if self.config.has_option("Stocks", StockSymbol):
			self.config.remove_option("Stocks", StockSymbol)

		else:
			print (StockSymbol, "has not been added")

		self.WriteFile()
		print ("Removed", StockSymbol)
		return True

	def WriteFile(self):
		with open('config.ini', 'w') as configfile:
			self.config.write (configfile)

		self.LoadConfigFile()

	def LoadConfigFile(self):
		self.File = self.config.read('config.ini')

	def GetAllStockSymbols(self):
		StockSymbols = [i for i in self.config.options("Stocks")]

		return StockSymbols