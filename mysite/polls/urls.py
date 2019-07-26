
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home_page, name="home_page"),
	path('index', views.index, name="index"),
    path('<int:question_id>',views.detail,name='detail'),
    path('<int:question_id>/result',views.result,name='result'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('nueva_pregunta',views.pregunta_crear,name='nueva_pregunta'),
    path('working_forms/', include('working_forms.urls')),
]
