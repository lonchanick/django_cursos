#from django.shortcuts import render
from django.http import HttpResponse
from . models import Question
from django.template import loader, RequestContext
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

from polls.form import PreguntaForm
from django.utils import timezone

# Create your views here.

def home_page(request):
	return render(request,'polls/home_page.html',{})

def index(request):
	latest_questions = Question.objects.order_by("-pub_date")[:5]
	context = {'latest_questions':latest_questions}
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Esta pregunta no existe jilipollas')
	return render(request, 'polls/detail.html',{'question':question})

def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/result.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except KeyError:
		return render(request,'polls/detail.html',{'question':question,'error_message':'No has elegido nada'})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('result', args=[question.id]))

def pregunta_crear(request):
	if request.method == "POST":
		form = PreguntaForm(request.POST)
		if form.is_valid():
			pregunta = Question(question_text = form.cleaned_data['pregunta'])
			pregunta.save()
			return HttpResponseRedirect('/polls')
	else:
		form = PreguntaForm()
		return render(request,'polls/pregunta_crear.html',{'form':form,'error_message':'No has elegido nada'})


