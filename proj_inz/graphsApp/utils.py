from typing import List
from django.apps import apps
from django.db.models import QuerySet
from .models import *
def recalculate_value(currency_in: str, value: float, currency: str) -> float:
    """
    Funkcja pobiera typ waluty, na który ma przeliczyć daną kryptowalutę
    Zwraca wartość w postaci float
    """
    # TODO Write a calculator form
    pass

def get_model_by_name(model_name: str) -> QuerySet:
    """
    Function that returns model object by its name
    """
    return (apps.all_models['graphs_App'])[model_name]

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
    

    

def get_unique_names_of_symbol_for_passed_model(model_name: str) -> List[str]:
    """
    Function returns distinct symbols for passed model and property_name
    """
    model = (apps.all_models['graphs_App'])[model_name]
    return list(model.objects.order_by().values_list('symbol', flat=True).distinct())

