from typing import OrderedDict
from django.db import models



class CurrencyRates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    eur = models.FloatField(db_column='EUR', blank=True, null=True)  # Field name made lowercase.
    usd = models.FloatField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    gbp = models.FloatField(db_column='GBP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currency_rates'
        ordering = ['date']
        
