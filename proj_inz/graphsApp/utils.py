from typing import List, Tuple, Dict
from django.apps import apps
from django.db.models import QuerySet
from .models import CurrencyRates, StockExchange, CryptoCurrencies
import pandas as pd
import json
import datetime
def recalculate_value(currency_in: str, value: float, currency: str) -> str:
    """
    Function takes currency type, amount of currency, and value from last model object \n
    Returns Price of passed amount of crypto
    """
    # ! Calculator handling
    dolar_to_pln = (CurrencyRates.objects.last()).usd
    result = round(float(value) * float(dolar_to_pln) * float(currency), 2)
    if currency_in == 'EUR':
        eur_to_pln = (CurrencyRates.objects.last()).eur
        result = round(result/float(eur_to_pln),2)
    elif currency_in == 'GBP':
        gbp_to_pln = (CurrencyRates.objects.last()).gbp
        result = round(result/float(gbp_to_pln),2)
    return f'Money needed to buy given amount of currency: {result} {currency_in}'

def get_model_by_name(model_name: str) -> QuerySet:
    """
    Function that returns model object by its name
    """
    return (apps.all_models['graphsApp'])[model_name]

def calculate_percent_diffrence(model_name: str, filter_symbol: str) -> float:
    """
    Function to calculate percent diffrence between two last records \n
    Model_Name. Name of model we're interested in \n
    Filter_Symbol. Symbol name which we're interested in
    """
    model = get_model_by_name(model_name)
    model_objects = model.objects.filter(symbol = filter_symbol).order_by('-id')[:2][::-1]
    if model_objects and model_name == 'cryptocurrencies':
        v1 = (model_objects[0]).value
        v2 = (model_objects[1]).value
        return round(((v2 - v1)/v1 * 100), 2)
    elif model_objects and model_name == 'stockexchange':
        v1 = (model_objects[0]).close_price
        v2 = (model_objects[1]).close_price
        return round(((v2 - v1)/v1 * 100), 2)
    else:
        raise Exception('Model with passed symbol doest not exists!')
    

def get_preview_data(data_model: QuerySet, symbol: str) -> Tuple[Dict[str, float], List[str]]:
    """
    Function to convert given model Queryset to propper object to display at page
    """
    preview_data = data_model.objects.filter(symbol = symbol).order_by('-date')[:25]
    dict_data = preview_data.values()
    keys = list(dict_data[0].keys())
    
    df = pd.DataFrame(data=dict_data)
    json_records = df.to_json(orient='records')
    json_df_obj = json.loads(json_records)
    
    for item in json_df_obj:
        for key, value in item.items():
            if key == 'date':
                item[key] = datetime.datetime.fromtimestamp(int(item[key])/1000)
            elif key == 'value' or 'price' in key:
                item[key] = round(item[key] , 4)
    
    return json_df_obj, keys
    

def get_unique_names_of_symbol_for_passed_model(model_name: str) -> List[str]:
    """
    Function returns distinct symbols for passed model and property_name
    """
    model = (apps.all_models['graphsApp'])[model_name]
    return list(model.objects.order_by().values_list('symbol', flat=True).distinct())



from decimal import Decimal
from plotly.offline import plot
from typing import Any
import plotly.graph_objects as go


def get_float_fields(record):
    return [key for key, value in record.items() 
        if isinstance(value, Decimal) or isinstance(value, float)]


def get_timestamp_fields(record):
    for key, value in record.items():
        if isinstance(value, datetime.date):
            return key   
    return None


def generate_graph(data) -> plot:
    if not data:
        raise ValueError('There is no values to plot.')

    datelike_col = get_timestamp_fields(data[0])

    if not datelike_col:
        raise ValueError('Cannot extract expected columns.')

    dates = [element.get(datelike_col) for element in data]
    graphs = [go.Scatter(x=dates, y=[element.get(numeric_col) for element in data],
         legendgroup="group1", legendgrouptitle_text = 'Dostępne zmienne:', mode='lines', name=numeric_col)
         for numeric_col in get_float_fields(data[0])]
    
    layout = {'template': 'plotly_white', 'legend_groupclick': 'toggleitem'}
    
    return plot(dict({'data': graphs, 'layout': layout}), output_type='div')

