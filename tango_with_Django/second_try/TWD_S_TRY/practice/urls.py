from django.urls import path
from . import views

app_name='practice'

urlpatterns = [
    path('', views.index,name='index'),
    path('templates/', views.templates,name='templates'),
    path('fields_types/', views.fields_types,name='fields_types'),
]