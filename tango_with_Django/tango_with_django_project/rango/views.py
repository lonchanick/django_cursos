from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context_dict={'boldmessage':'Que coño es rango?'}
	return render(request,'rango/index.html',context=context_dict)

def about(request):
	context_dict={'boldmessage':'This is "about.html" page'}
	return render(request,'rango/about.html',context=context_dict)

def israel(request):
	return render(request,'rango/israel.html',{})