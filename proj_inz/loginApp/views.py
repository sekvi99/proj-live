from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

"""
In this file you will find a description of the views that are responsible for handling the user login system
In the project we adopted the function-based-view assumption (i.e. we describe behavior with the help of functions)
"""


"""
The login function is responsible for the correct handling of user login to the application

1 First, we check if the user is authenticated i.e. has a token that allows access to the application.
1a) If the user is already logged in then he is redirected to the home page, in the graps application (There is no need to log the user in again).
1b) In the opposite case we move on -> because we know that the user is not logged in
2) Then we check the type of request that comes to the application, we want to handle POST. ==> If it is a post, we retrieve the content of the data given in the form.
3.Then we try to find the user with the given login data in the database. ==> If such exists, we log the user in otherwise we return the appropriate message.

The function on the output returns a render object, which consists of:
1. the request,
2. the name of the template to be generated after connecting to the given url,
3. the context object => a dictionary, with the data that we pass to the template.
"""
# ! User login support
def login_page(request):
  table_name = 'Login'
  if request.user.is_authenticated:
    return redirect('graphsApp:home')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
        user = User.objects.get(username=username)
      except:
        messages.error(request, "The specified user does not exist in the database!")

      user = authenticate(request, username=username, password=password) 
      if user is not None:
        login(request, user) 
        messages.success(request, f'Successfully logged in - Welcome {request.user.username}!')
        return redirect('graphsApp:home')
      else:
        messages.error(request, 'User login or password is incorrect!')

    context = {'table_name':table_name}
    return render(request, 'login.html', context)

"""
The logout function using the ready-made logout method actually removes the weatherization token and redirects the user to another page
"""
# ! User logout support
def logout_page(request):
  
    logout(request)
    messages.success(request, f"Successfully logged out!")
    return redirect('login_App:login')
