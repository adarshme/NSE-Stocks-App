# NSE-Stocks-App
Quickly get information about your stocks through a CLI or GUI.

You need Python 3 installed. Instructions to add your stocks and run the program are given in the comments.

Note:- This is still in development. Stay tuned for more features!

Required modules (Not in stdlib)-
  Beautiful Soup 4
  
Optional modules -
  PyQT5 (For GUI)

Instructions:-
 List of commands available: -
   1) get all
   2) get
   3) add
   4) remove
   5) status

   1) get all:-
     Use 'get all' to show all your stock values.

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
   python3 cli.py COMMAND
