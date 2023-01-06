from cgi import test
from locale import currency
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .forms import calculatorForm
from .utils import recalculate_value, generate_graph
from .models import CryptoCurrencies, StockExchange, CurrencyRates
from .utils import get_unique_names_of_symbol_for_passed_model, calculate_percent_diffrence, get_model_by_name, get_preview_data
from django.contrib.contenttypes.models import ContentType
from typing import Final
from django.forms.models import model_to_dict


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
    crypto_percentage = [calculate_percent_diffrence('cryptocurrencies',crypto) for crypto in unqiue_crypto] # ! Getting percentage change of values for crypto
    stock_percentage = [calculate_percent_diffrence('stockexchange',stock) for stock in unique_stock] # ! Getting percentage change of values for stocks
    
    try:
        crypto_model = get_model_by_name('cryptocurrencies')
        stock_model = get_model_by_name('stockexchange')
        data = [crypto_model.objects.filter(symbol = crypto).values('date', 'value', 'symbol').last() for crypto in unqiue_crypto] + \
            [stock_model.objects.filter(symbol = stock).values('date', 'close_price', 'symbol').last() for stock in unique_stock]
        
    except Exception:
        pass
        
    
    keys = ['Data', 'Wartość', 'Znacznik']
    context ={'table_name':table_name,
              'headers':keys,
              'json_file':data
              }
    return render(request, 'graphsApp/dashboard.html',context)

@login_required(login_url='/login/')
def about_authors(request):
    """
    Function view for 'authors'
    """
    authors: Final[list] = [
        {'name':'Filip', 'second_name':'Kozlik'},
        {'name':'Wojciech', 'second_name':'Kubak'},
        {'name':'Wojciech', 'second_name':'Harmata'},
    ]
    context = {
        'authors':authors,
    }
    return render(request, 'graphsApp/about.html', context)

@login_required(login_url='/login/')
def data_view(request, tablename: str, symbol: str):
    currency_description = None  # ! Tutaj opis dla kazdej waluty, ktora posiadamy (mozna po slowniku)
    form = calculatorForm() 
    dict_data = None
    calc_value = None
    global data
    table_values = None
    table_keys = None
    graph = None
    symbol = symbol.capitalize() if tablename == 'cryptocurrencies' else symbol.upper()
    situation_message = calculate_percent_diffrence(tablename, symbol)
    try:
        data_model = get_model_by_name(tablename)
        data = data_model.objects.filter(symbol=symbol).last()
        graph = generate_graph(data_model.objects.filter(symbol=symbol).values())
        dict_data = model_to_dict(data)
        table_values, table_keys = get_preview_data(data_model, symbol)
        
    except Exception as e:
        print(str(e))
    
    if 'form' in request.POST:
        try:
            form = calculatorForm(data = request.POST)
            if form.is_valid():
                value = float(form.data['value'])
                currency_in = form.data['currency_in']
                obj_value = data.value if tablename =='cryptocurrencies' else data.close_price
                """
                Function takes:
                1. Currency_in => Type of currency to calculate,
                2. Value => Value from form on page,
                3. Obj_value => Value of last 
                """
                calc_value = recalculate_value(currency_in, value, obj_value)

        except Exception as e:
            print(str(e))
    
    context = dict({
        'table_name' : symbol,
        'data':dict_data,
        'situation_message' : situation_message,
        'currency_description': currency_description,
        'form':form,
        'calc_value':calc_value,
        'table_values':table_values,
        'table_keys':table_keys,
        'graph': graph
    })
    return render(request, 'graphsApp/detailsPage.html', context)
    