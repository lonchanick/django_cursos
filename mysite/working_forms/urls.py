
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="working_forms"),
	path('thanks', views.thanks, name="thanks"),
	path('ejemplo_1', views.ejemplo_1, name="ejemplo_1"),
	path('ejemplo_2', views.ejemplo_2, name="ejemplo_2"),
]
