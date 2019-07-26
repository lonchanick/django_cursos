
from django.urls import path
from . import views

urlpatterns = [
	path('', views.modelos, name="modelos"),
]


"""
    path('anotherQuestion', views.anotherQuestion, name="anotherQuestion"),
    path('<int:question_id>',views.detail,name='detail'),
    path('<int:question_id>/result',views.result,name='result'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('nueva_pregunta',views.pregunta_crear,name='nueva_pregunta')
"""