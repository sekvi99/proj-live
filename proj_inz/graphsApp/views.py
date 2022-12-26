from cgi import test
from locale import currency
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import calculatorForm
from .utils import recalculate_value
from .models import *
# Create your views here.
# ! test - view to check wheth er login works porpperly


@login_required(login_url='/login/')
def home(request):
    table_name = 'Strona główna'
    querySet = CurrencyRates.objects.all()
    dict_data = querySet.values()
    keys = list(dict_data[0].keys())
    context ={'table_name':table_name,
              'headers':keys,
              'json_file':dict_data
              }
    #context = dict({})
    return render(request, 'graphsApp/dashboard.html',context)

@login_required(login_url='/login/')
def data_view(request):
    situation_message = None # ! Tutaj zaleznie od tego czy cena rosnie czy maleje nalezy dac stosowny komunikat
    currency_description = None  # ! Tutaj opis dla kazdej waluty, ktora posiadamy (mozna po slowniku)
    form = calculatorForm() # ! Tutaj klasa formularza
    data_name = request.GET('q') if request.GET('q') != None else ''
    currency = None
    #  data_name.objects.filter(symbol__icontains = '').last()
    
    if request.method == 'POST':
        try:
            form = calculatorForm(data = request.POST)
            if form.is_valid():
                value = float(form.data['value'])
                currency_in = form.data['currency_in']
                """
                Function takes:
                1. Currency_in => Type of currency to calculate,
                2. Value => Value from form on page,
                3. Currency => Name of model
                """
                recalculate_value(currency_in, value, currency)
        except Exception as e:
            print(str(e))
    
    context = dict({
        'table_name' : data_name,
        'sitution_message' : situation_message,
        'currency_description': currency_description,
        'form':form,
    })
    return render(request, 'graphsApp/dataView.html', context)
    