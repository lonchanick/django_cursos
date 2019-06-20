
from django.urls import path

from . import views

""" Esta cagada tambien esta modificada para usar el tal sistema de platillas ese """
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


"""
#si se activa este codigo y se suspende el que esta mas arriba hay que
#activar el codigo que esta en las views tambien

from django.urls import path
from . import views

app_name ='polls'
urlpatterns = [
	# ejemplo: /polls/
	path('', views.index,name='index'),
	# ejemplo: /polls/5/
	path('<int:question_id>/', views.detail,name='detail'),
	# ejemplo: /polls/5/results
	path('<int:question_id>/results/', views.results,name='results'),
	# ejemplo: /polls/5/results
	path('<int:question_id>/vote/', views.vote,name='vote'),

]
"""
