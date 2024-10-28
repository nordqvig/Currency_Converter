# Currency Converter (in progress)

### Currency converter that uses yfinance to fetch exchange rates and convert amounts in different currencies.

A python implementation of a currency converter which allows users to convert an amount of one currency into 
the equivalent amount of a different currency.   

### Installation

With python 3, download the Currency_Converter.py file and run commands from terminal according to syntax described by API.


### Documentation

#### class _Currency Converter_
    class CurrencyConverter:

Creates a currency converter object.

#### method _ConvertCurrency_
    method ConvertCurrency(self, currency1, currency2, amount1)

Converts the amount (_amount1_) of the currency (_currency1_) into the equivalent amount (_amount2_) in the new currency (_currency2_).
Returns the result as an array as follows: [currency2, _amount2_]
+ _currency1_ and _currency2_ are passed as strings in format: # TODO
+ _amount1_ is passed as a positive float value

### Roadmap

- The API of this library will not be changed unless to deal with issues that can't be resolved in any other way. 
- Version numbers follow semantic versioning. 


