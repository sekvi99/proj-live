from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

"""
W tym pliku znajdujue się opis widoków, które są odpowiedzialne za obsłużenie systemu logowania użytkownika
W projekcie przyjeliśmy założenie function-based-view (czyli zachowania opisujemy z pomocą funkcji)
"""


"""
Funkcja login jest odpowiedzialna za poprawne obsłużenie logowania użytkownika do aplikacji

1. Na początku sprawdzamy czy użytkownik jest authenticated tzn. czy posiada token, który umożliwia dostęp do aplikacji.
1a) Jeżeli użytkownik jest już zalogowany to jest on przekierowywane na stronę home, w aplikacji graps (Nie ma potrzeby ponownego logowania użytkownika).
1b) W przeciwynm przypadku przechodzimy dalej -> gdyż wiemy, że utkownik nie jest zalogowany
2. Następnie sprawdzamy typ requesta, który przychodzi do aplikacji, chcemy obsłużyć POST. ==> Jeżeli jest to post, to pobieramy zawartość danych podanych w formularzu.
3. Następnie staramy znaleźć się użytkownika o podanych danych logowania w bazie. ==> Jeżeli taki istnieje, to logujemy użytkownika w przeciwnym razie zwracamy stosowny komunikat.

Funkcja na wyjściu zwraca obiekt render, który składa się z:
1. Request'a,
2. Nazwy template'a, który ma zostać wygenerowany po połączeniu się z danym url'em,
3. Obiekt context => słownik, z danymi który przekazujemy do template'a.
"""
# ! Obsługa logowania użytkownika
def loginPage(request):
  table_name = 'Login'
  if request.user.is_authenticated:
    return redirect('graph_App:home')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
        user = User.objects.get(username=username)
      except:
        messages.error(request, "Podany użytkownik nie istnieje w bazie danych!")

      user = authenticate(request, username=username, password=password) 
      if user is not None:
        login(request, user) 
        messages.success(request, f'Pomyślnie zalogowano - Witaj {request.user.username}!')
        return redirect('graph_App:home')
      else:
        messages.error(request, 'Login lub hasło użytkownika jest niewłaściwe!')

    context = {'table_name':table_name}
    return render(request, 'login.html', context)

"""
Funkcja logout z użyciem gotowej metody logout usuwa w rzeczywistości token uwietrzylniający i przekierowuje użytkownika na inną stronę
"""
# ! Obsługa wylogowywania użytkownika
def logoutPage(request):
    table_name = 'Strona Wyjściowa'
    logout(request)
    context = {'table_name':table_name}
    return render(request, 'logout.html', context)