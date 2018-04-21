# NSE-Stocks-App
Cross Platform App to quickly get real-time information about your stocks through a *CLI* or *GUI*.

> The *National Stock Exchange of India Limited* (NSE) is the leading stock exchange of India, located in Mumbai. 

You need Python 3 installed. Instructions to add your stocks and run the program are given [below](https://github.com/InfernoCoder11/NSE-Stocks-App#instructions-).

Note:- **This is still in development. Stay tuned for more features!** Any suggestions are always welcome.

***Required modules*** (Not in stdlib)-
  ***Beautiful Soup 4***
  
Optional modules -
  *PyQT5* (For GUI)

## Instructions:-
 List of commands available: -
   - get all
   - get
   - add
   - remove
   - status

   1. get all:-
     Use `get all` to show all your stock values sequentially but may be slower.
     Use `get all-m` to get faster results, but stocks are shown randomly.

   2. get:-
     Use `get STOCKSYMBOLS` to get the values of particular stocks.

   3. add:-
     Use `add STOCKSYMBOLS` to add stocks to the list of all your stocks.

   4. remove:-
     Use `remove STOCKSYMBOLS` to remove stocks from your list of stocks.

   5. status:-
     Use `status` to see your list of stocks

 Wherever *STOCKSYMBOLS* have been used, it means you can use a single stock symbol or multiple stock symbols seperated by spaces.
 If you would prefer another printing format, check out [Stocks.py](https://github.com/InfernoCoder11/NSE-Stocks-App/blob/master/Stocks.py).

 To call a command, type:-
   `python cli.py COMMAND`

 if you are in a system which has python2 by default, type:-
   `python3 cli.py COMMAND`

### How to install python and/or required modules:-
   1. Download the latest version of python (3.x.x) from [here](https://www.python.org/downloads/) and install it.
   2. In terminal/cmd/powershell type `pip install beautifulsoup4` to install BeautifulSoup4.
   3. To install PyQt5, type `pip install pyqt5`.
   - If you already have python 3 installed, skip the first step.
   - Note that some OS's ship with python 2 and python 3 pre-installed. In that case replace pip with pip3.

*Developed and tested extensively on Ubuntu 16.04 LTS. Some aesthetic features are disabled for windows due to non-compatibility. Will update as soon as a solution is found. April 21 2018.*
