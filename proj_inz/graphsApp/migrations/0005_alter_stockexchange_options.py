# Generated by Django 4.0.6 on 2023-01-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphsApp', '0004_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockexchange',
            options={'managed': False, 'ordering': ['date']},
        ),
    ]