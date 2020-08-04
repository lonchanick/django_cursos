parrafo="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, \nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit \nesse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

lista=['nombre','casa',None,3.1516,1991]

from django.shortcuts import render
from django.http import HttpResponse
from practice.models import Comment,Post
from practice.forms import Fields_types_form

# Create your views here.
def index(request):
	return render(request,'practice/index.html',{})
	

def templates(request):
	posts=Post.objects.all()
	ob={'title':'Hola mundo'}
	d1={
	'escape':'<h1>{{text|safe}}</h1>',
	'name':'israel',
	'last_name':'arroyo',
	'age':'28',
	'object':ob,
	'title':'Atributo Title \ndel diccionario context',
	'parrafo':parrafo,
	'lista':lista,
	'value':None,
	'size_file':123412545234,
	'raw_text':'<script>alert(\'hello\')</script>',
	'posts':posts
	}

	return render(request,'practice/templates.html',{'context':d1})
	
def fields_types(request):
	form=Fields_types_form()
	return render(request,'practice/fields_types.html',{'form':form})
	