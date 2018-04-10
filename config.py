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

		else:
			print ("Couln't find", StockSymbol)

	def RemoveStockSymbol(self, StockSymbol):
		self.config.remove_option("Stocks", StockSymbol)

		self.WriteFile()

	def WriteFile(self):
		with open('config.ini', 'w') as configfile:
			self.config.write (configfile)

		self.LoadConfigFile()

	def LoadConfigFile(self):
		self.File = self.config.read('config.ini')


Config = Config()

Config.AddStockSymbol("Infy")