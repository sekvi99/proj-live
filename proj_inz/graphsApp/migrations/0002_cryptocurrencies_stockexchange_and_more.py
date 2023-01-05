# Generated by Django 4.0.6 on 2023-01-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrencies',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('value', models.FloatField(blank=True, db_column='Value', null=True)),
                ('coin_symbol', models.CharField(blank=True, db_column='Coin_Symbol', max_length=50, null=True)),
            ],
            options={
                'db_table': 'crypto_currencies',
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
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='currencyrates',
            options={'managed': False},
        ),
    ]