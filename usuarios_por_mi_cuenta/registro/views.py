from django.shortcuts import render
from django.http import HttpResponse
from registro.models import Usuario, Pregunta
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index():
	pass

def home(request):
	return render(request,'registro/home.html')

def add_user(request):
	return render(request,'registro/add_user.html')

def list_users(request):
	list_users = Usuario.objects.order_by("-fecha_reg")[:100]
	context = {'list_users':list_users}
	return render(request,'registro/list_users.html',context)

def save_user(request, nombre):
	new_user = Usuario(nombre=nombre, nickname="self.nickname", passw="self.passw")
	new_user.save()
	return HttpResponseRedirect(reverse('list_users'))