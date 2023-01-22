from django.urls import path, include
from . import views

app_name = 'graphsApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('authors', views.about_authors, name='authors'),
    path('data/<str:tablename>/<str:symbol>', views.data_view, name='data'),
    path('<str:datatype>', views.filtered_home_view, name='filtered-home-view'),
    #path()
]