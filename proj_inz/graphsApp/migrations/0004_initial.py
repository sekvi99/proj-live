# Generated by Django 4.0.6 on 2023-01-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('graphsApp', '0003_delete_cryptocurrencies_delete_currencyrates_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrencies',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('value', models.FloatField(blank=True, db_column='Value', null=True)),
                ('symbol', models.CharField(blank=True, db_column='Coin_Symbol', max_length=50, null=True)),
            ],
            options={
                'db_table': 'crypto_currencies',
                'ordering': ['date'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CurrencyRates',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('eur', models.FloatField(blank=True, db_column='EUR', null=True)),
                ('usd', models.FloatField(blank=True, db_column='USD', null=True)),
                ('gbp', models.FloatField(blank=True, db_column='GBP', null=True)),
            ],
            options={
                'db_table': 'currency_rates',
                'ordering': ['date'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('open_price', models.FloatField(blank=True, db_column='Open_Price', null=True)),
                ('high_price', models.FloatField(blank=True, db_column='High_Price', null=True)),
                ('low_price', models.FloatField(blank=True, db_column='Low_Price', null=True)),
                ('close_price', models.FloatField(blank=True, db_column='Close_Price', null=True)),
                ('volume', models.FloatField(blank=True, db_column='Volume', null=True)),
                ('symbol', models.CharField(blank=True, db_column='Symbol', max_length=50, null=True)),
            ],
            options={
                'db_table': 'stock_exchange',
                'ordering': ['-date'],
                'managed': False,
            },
        ),
    ]