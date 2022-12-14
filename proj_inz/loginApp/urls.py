from django.urls import path, include
from . import views
app_name = 'login_App'
urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]