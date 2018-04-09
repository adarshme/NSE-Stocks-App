import configparser
import Stocks

StockApp = Stocks.Stocks()

class Config():
	def __init__(self):
		config = configparser.ConfigParser()

		File = config.read('config.ini')

	def AddStockSymbol(self, StockSymbol):
		try:
			Data = StockApp.ExtractStockPrice(StockSymbol)
		except IndexError:
			Data = None

		if Data:
			print (True)

		else:
			print (False)

Config = Config()

Config.AddStockSymbol("INFY")