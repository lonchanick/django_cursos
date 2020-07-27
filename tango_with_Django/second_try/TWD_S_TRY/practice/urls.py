from django.urls import path
from . import views

app_name='practice'

urlpatterns = [
    path('', views.index,name='index'),
    path('templates/', views.templates,name='templates'),
]