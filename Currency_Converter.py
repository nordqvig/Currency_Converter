import requests
import yfinance as yf

msft = yf.Ticker("USDSEK=X")
print(msft.info)

class CurrencyConverter:
    "Class to convert amounts in one currency (currency1) into the equivalent amount in another currency currency2. "
    def __init__(self, amount, currency1, currency2):
        """Initiates the class instance with the following attributes:
        self.currency1 - the currency to be converted FROM
        self.currency2 - the currency to be converted TO
        self.amount =  the amount of currency1 that will be converted into currency2 """
        self.amount = amount
        self.currency1 = currency1
        self.currency2 = currency2
        self.Xrate = None # The yfinance call to the 'Ticker' of the exchange rate will be made here.

    "Method to perform the conversion. Returns the amount in currency 2 that the amount of currency 1 is equivalent to."
    def convert(self):
        pass



