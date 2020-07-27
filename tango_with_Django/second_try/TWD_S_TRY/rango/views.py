from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	ctx={'boldmessage':'este es el famoso boldmessage'}
	return render(request,'rango/index.html',ctx)

def home_page(request):
	return render(request,'rango/base.html',{})

def about(request):
	return render(request,'rango/about.html',{})

