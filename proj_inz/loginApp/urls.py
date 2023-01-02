from django.urls import path, include
from . import views
app_name = 'login_App'
urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]