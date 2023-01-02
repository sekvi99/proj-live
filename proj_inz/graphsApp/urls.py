from django.urls import path, include
from . import views

app_name = 'graphs_App'
urlpatterns = [
    path('', views.home, name='home'),
    path('authors', views.about_authors, name='authors'),
    path('data/<str:tablename>/<str:symbol>', views.data_view, name='data')
]