# NSE-Stocks-App
Quickly get information about your stocks through a *CLI* or *GUI*.

> The *National Stock Exchange of India Limited* (NSE) is the leading stock exchange of India, located in Mumbai . 

You need Python 3 installed. Instructions to add your stocks and run the program are given [below](https://github.com/InfernoCoder11/NSE-Stocks-App#instructions-).

Note:- __This is still in development. Stay tuned for more features!__ Any suggestions are always welcome.

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

   1) get all:-
     Use `get all` to show all your stock values sequentially but may be slower.
     Use `get all-m` to get faster results, but stocks are shown randomly.

   2) get:-
     Use `get STOCKSYMBOLS` to get the values of particular stocks.

   3) add:-
     Use `add STOCKSYMBOLS` to add stocks to the list of all your stocks.

   4) remove:-
     Use `remove STOCKSYMBOLS` to remove stocks from your list of stocks.

   5) status:-
     Use `status` to see your list of stocks

 Wherever *STOCKSYMBOLS* have been used, it means you can use a single stock symbol or multiple stock symbols seperated by spaces.
 If you would prefer another printing format, check out [Stocks.py](https://github.com/InfernoCoder11/NSE-Stocks-App/blob/master/Stocks.py)

 To call a command, type:-
   `python cli.py COMMAND`

 if you are in a system which has python2 by default, type:-
   `python3 cli.py COMMAND`

*New CLI Features! Check them out! April 11 2018*
