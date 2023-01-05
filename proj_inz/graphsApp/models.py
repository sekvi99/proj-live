from typing import OrderedDict
from django.db import models

# ! Data ordering => ordering = ['date']
# ! App Label => app_label = 'graph_App'

"""
List of models (representation of database), used in graphs application
"""

class CryptoCurrencies(models.Model):
    """
    ID. Autoincremented int field \n
    Date. Date in format Y-m-d \n
    Value. Value of given coin at given date \n
    Symbol. Symbol representation of given coin
    """
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Coin_Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self) -> str:
        """
        Object string representation for admin panel object description for Crypto Currencies
        """
        return f'Waluta: {self.symbol}, data: {self.date}'

    class Meta:
        managed = False
        db_table = 'crypto_currencies'
        app_label = 'graphsApp'
        ordering = ['date']


class CurrencyRates(models.Model):
    """
    ID. Autoincremented int field \n
    Date. Date in format Y-m-d \n
    EUR. EUR rate for given date \n
    USD. USD rate for given date \n
    GBP. GBP rate for given date
    """
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    eur = models.FloatField(db_column='EUR', blank=True, null=True)  # Field name made lowercase.
    usd = models.FloatField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    gbp = models.FloatField(db_column='GBP', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        """
        Object string representation for admin panel object description for Currency Rates
        """
        return f'Kursy walut z dnia: {self.date}'

    class Meta:
        managed = False
        db_table = 'currency_rates'
        app_label = 'graphsApp'
        ordering = ['date']


class StockExchange(models.Model):
    """
    ID. Autoincremented int field \n
    Date. Date in format Y-m-d \n
    OPEN_PRICE. Open price for given date \n
    HIGH_PRICE. Highest price for given company at given date \n
    LOW_PRICE. Lowest price for given company at given date \n
    Volume. Volume of transcations for given date \n
    Symbol. Symbol representation for given company
    """
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open_price = models.FloatField(db_column='Open_Price', blank=True, null=True)  # Field name made lowercase.
    high_price = models.FloatField(db_column='High_Price', blank=True, null=True)  # Field name made lowercase.
    low_price = models.FloatField(db_column='Low_Price', blank=True, null=True)  # Field name made lowercase.
    close_price = models.FloatField(db_column='Close_Price', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        """
        Object string representation for admin panel object description for Stock Exchange
        """
        return f'Kursy dla: {self.symbol} z dnia: {self.date}'

    class Meta:
        managed = False
        db_table = 'stock_exchange'
        app_label = 'graphsApp'
        ordering = ['date']
