# Run this program to get Stocks info through a GUI.

import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel)
from PyQt5.QtCore import Qt
import Stocks
import time

StockApp = Stocks.Stocks()

class Window (QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui (self):
		self.EnterStockSymbol = QLineEdit()
		self.EnterStockSymbol.setPlaceholderText ("Type Stock Symbol Here!")
		self.SearchButton = QPushButton('Search')

		self.LastPriceLabel = QLabel()
		self.PChangeLabel = QLabel()
		self.ChangeLabel = QLabel()
		self.LUTLabel = QLabel ()
		self.StockNameLabel = QLabel ()

		self.setGeometry (300, 200, 300, 200)

		self.v_box = QVBoxLayout()

		self.v_box.addWidget (self.EnterStockSymbol)
		self.v_box.addWidget (self.SearchButton)

		self.v_box.addWidget (self.StockNameLabel)
		self.v_box.addWidget (self.LastPriceLabel)
		self.v_box.addWidget (self.PChangeLabel)
		self.v_box.addWidget (self.ChangeLabel)
		self.v_box.addWidget (self.LUTLabel)

		self.setLayout(self.v_box)
		self.setWindowTitle('Stock Price Search')

		self.SearchButton.clicked.connect(self.btn_clk)
		self.EnterStockSymbol.returnPressed.connect(self.btn_clk)

		self.show()

	def btn_clk(self):
		try:
			QApplication.setOverrideCursor(Qt.WaitCursor)

			Data = StockApp.ExtractStockPrice(self.EnterStockSymbol.text().upper())

			if "list index out of range" in Data:
				raise ValueError ("Something wrong with the Stock Symbol Entered")

			self.lastPrice = StockApp.lastPrice
			self.pChange = StockApp.pChange
			self.change = StockApp.change
			self.lastUpdateTime = StockApp.lastUpdateTime
			self.companyName = StockApp.companyName

			self.StockNameLabel.setText (self.companyName)
			self.LastPriceLabel.setText ("Last Price: " + self.lastPrice)
			self.PChangeLabel.setText ("Percentage Change: " + self.pChange)
			self.ChangeLabel.setText ("Absolute Change: " + self.change)
			self.LUTLabel.setText ("Last Updated: " + self.lastUpdateTime)

			QApplication.restoreOverrideCursor()

		except Exception:
			QApplication.setOverrideCursor(Qt.ForbiddenCursor)
			time.sleep (0.5)
			QApplication.setOverrideCursor(Qt.ArrowCursor)
			pass





app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())