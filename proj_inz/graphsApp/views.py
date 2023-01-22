from cgi import test
from locale import currency
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .forms import calculatorForm
from .utils import recalculate_value, generate_graph
from .models import CryptoCurrencies, StockExchange, CurrencyRates
from .utils import get_unique_names_of_symbol_for_passed_model, calculate_percent_diffrence, get_model_by_name, get_preview_data
from django.contrib.contenttypes.models import ContentType
from typing import Final, List
from django.forms.models import model_to_dict
from json import dumps

TABLE_NAMES:Final[str] = list([
    'cryptocurrencies', 
    'stockexchange',
])

"""
Home display table in given order
|Symbol|Date|Last Price|Diffrence between Last Two as %|
"""
@login_required(login_url='/login/')
def home(request):
    """
    Function view for base url ''
    """
    table_name = 'Main Page'
    global data
    keys = None
    unqiue_crypto = get_unique_names_of_symbol_for_passed_model('cryptocurrencies') # ! Getting unique coins for crypto currencies
    unique_stock = get_unique_names_of_symbol_for_passed_model('stockexchange') # ! Getting unique companies for stock exchange
    # crypto_percentage = [calculate_percent_diffrence('cryptocurrencies',crypto) for crypto in unqiue_crypto] # ! Getting percentage change of values for crypto
    # stock_percentage = [calculate_percent_diffrence('stockexchange',stock) for stock in unique_stock] # ! Getting percentage change of values for stocks
    
    try:
        crypto_model = get_model_by_name('cryptocurrencies')
        stock_model = get_model_by_name('stockexchange')
        data = [crypto_model.objects.filter(symbol = crypto).values('date', 'value', 'symbol').last() for crypto in unqiue_crypto] + \
            [stock_model.objects.filter(symbol = stock).values('date', 'close_price', 'symbol').last() for stock in unique_stock]
    except Exception as e:
        print(str(e))
    
    keys = ['Data', 'Wartość', 'Znacznik']
    context ={'table_name':table_name,
              'headers':keys,
              'json_file':data,
              'unqiue_crypto':unqiue_crypto,
              'unique_stock':unique_stock,
              }
    return render(request, 'pages/dashboard.html',context)

# /stockexchange/

@login_required(login_url='/login/')
def filtered_home_view(request, datatype: str) -> render:
    """
    View for data filtering in home page => crypto, stock
    """
    table_name = 'Filtered Home View'
    data = None
    keys = None
    unqiue_crypto = get_unique_names_of_symbol_for_passed_model('cryptocurrencies') # ! Getting unique coins for crypto currencies
    unique_stock = get_unique_names_of_symbol_for_passed_model('stockexchange') # ! Getting unique companies for stock exchange
    try:
        if datatype == 'cryptocurrencies':
            crypto_model = get_model_by_name('cryptocurrencies')
            data = [crypto_model.objects.filter(symbol = crypto).values('date', 'value', 'symbol').last() for crypto in unqiue_crypto]
        elif datatype == 'stockexchange':
            stock_model = get_model_by_name('stockexchange')
            data = [stock_model.objects.filter(symbol = stock).values('date', 'close_price', 'symbol').last() for stock in unique_stock]
        elif datatype not in TABLE_NAMES:
            return redirect('graphsApp:home')
    except Exception as e:
        print(str(e))
        
    
    keys = ['Data', 'Wartość', 'Znacznik']
    context ={'table_name':table_name,
              'headers':keys,
              'json_file':data,
              'unqiue_crypto':unqiue_crypto,
              'unique_stock':unique_stock,
              }
    return render(request, 'pages/dashboard.html',context)

@login_required(login_url='/login/')
def about_authors(request):
    """
    Function view for 'authors'
    """
    authors: Final[list] = [
        {'name':'Filip Koźlik', 'second_name':'Kozlik'},
        {'name':'Wojciech Kubak', 'second_name':'Kubak'},
        {'name':'Wojciech Harmata', 'second_name':'Harmata'},
    ]
    techstack: Final[list] = [
        {'title': 'Accordion #1', 'body': 'Example body string 1.'},
        {'title': 'Accordion #2', 'body': 'Massa tempor nec feugiat nisl pretium. In arcu cursus euismod quis viverra nibh cras. Orci porta non pulvinar neque laoreet suspendisse. A lacus vestibulum sed arcu non. Semper quis lectus nulla at volutpat diam ut venenatis tellus.'},
        {'title': 'Accordion #3', 'body': 'Example body string 3.'},
        {'title': 'Accordion #4', 'body': 'Example body string 4.'},
        {'title': 'Accordion #5', 'body': 'Example body string 5.'},
        {'title': 'Accordion #6', 'body': 'Example body string 6.'},
        {'title': 'Accordion #7', 'body': 'Example body string 7.'},
        {'title': 'Accordion #8', 'body': 'Example body string 8.'}
    ]
    context = {
        'authors':authors,
        'techstack': techstack,
    }
    return render(request, 'pages/about.html', context)


# def item_details(request, item, category) FIXME: <-jak tutaj nazwy properties
@login_required(login_url='/login/')
def data_view(request, tablename: str, symbol: str):
    table_keys = None
    dict_data = None
    table_values = None
    graph = None
    exchange_rates = None
    if tablename not in TABLE_NAMES:
        return redirect('graphsApp:home')
    try:
        data_model = get_model_by_name(tablename)
        data = data_model.objects.filter(symbol=symbol).last()
        graph = generate_graph(data_model.objects.filter(symbol=symbol).values())
        dict_data = model_to_dict(data)
        table_values, table_keys = get_preview_data(data_model, symbol)
        

        exchange_rates = dict({
            'value': dict_data.get('value') if tablename =='cryptocurrencies' else dict_data.get('close_price'),
            'usd': CurrencyRates.objects.last().usd,
            'eur': CurrencyRates.objects.last().eur,
            'gbp': CurrencyRates.objects.last().gbp
        })

    except Exception as e:
        print(str(e))

    context = dict({
        'table_name' : symbol,
        'data':dict_data,
        'table_values':table_values,
        'table_keys':table_keys,
        'graph': graph,
        'exchange_rates': dumps(exchange_rates)
    })
    return render(request, 'pages/details.html', context)


    