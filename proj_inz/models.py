# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CryptoCurrencies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    coin_symbol = models.CharField(db_column='Coin_Symbol', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crypto_currencies'


class CurrencyRates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    eur = models.FloatField(db_column='EUR', blank=True, null=True)  # Field name made lowercase.
    usd = models.FloatField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    gbp = models.FloatField(db_column='GBP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currency_rates'


class StockExchange(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open_price = models.FloatField(db_column='Open_Price', blank=True, null=True)  # Field name made lowercase.
    high_price = models.FloatField(db_column='High_Price', blank=True, null=True)  # Field name made lowercase.
    low_price = models.FloatField(db_column='Low_Price', blank=True, null=True)  # Field name made lowercase.
    close_price = models.FloatField(db_column='Close_Price', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_exchange'
