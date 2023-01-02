from django.contrib import admin

from .models import CurrencyRates, CryptoCurrencies, StockExchange

# ! Application Data models
admin.site.register(CurrencyRates)
admin.site.register(CryptoCurrencies)
admin.site.register(StockExchange)