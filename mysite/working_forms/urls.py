
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="working_forms"),
	path('ejemplo_1', views.ejemplos, name="ejemplo_1"),
	path('ejemplo_2', views.ejemplo_2, name="ejemplo_2"),
]
