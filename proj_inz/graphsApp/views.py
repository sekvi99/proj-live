from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# ! test - view to check whether login works porpperly

@login_required(login_url='/login/')
def home(request):
    table_name = 'Strona główna'
    context ={'table_name':table_name, 'message':'Test'}
    return render(request, 'graphsApp/home.html',context)