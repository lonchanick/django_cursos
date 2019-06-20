from django.shortcuts import render
from django.http import HttpResponse


def modelos(request):
	return HttpResponse("Hola desde modelos")
