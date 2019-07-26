from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path('add_user',views.add_user, name="add_user"),
	path('list_users',views.list_users, name="list_users"),
	#path('<str:xyz>/save_user',views.save_user, name="save_user"), #<str:nombre>/
	path(r'^registro/save_user/(?P<nombre>\s+)/$',views.save_user, name="save_user"), #<str:nombre>/
	
]
 