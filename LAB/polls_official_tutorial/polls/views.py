from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from polls.models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
def questions_startswith(request):
	q=Question.objects.filter(question_text__startswith='ultra')
	
	if q:
		return render(request,'polls/question_startswith.html',{'q':q})
	else:
		raise Http404('No hay preguntas que correspondan a ese patron de busqueda')

class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		return Question.objects.all()

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
	context_object_name='q'

class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'
	context_object_name='q'


def vote(request,question_id):
	q=get_object_or_404(Question,id=question_id)
	try:
		ch=q.choice_set.get(id=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		context={
		'q':q,
		'error_message':'U didn\'t select a choice',
		}
		return render(request,'polls/detail.html',context)
	
	else:
		ch.votes+=1
		ch.save()
		return HttpResponseRedirect(reverse('polls:results',args=(q.id,) ))


'''
#OLD VIEWS
def index(request):
	try:
		latest_question_list=Question.objects.order_by('pub_date')

	except Question.DoesNotExist:
		raise Http404('Question does not exist')

	return render(request,'polls/index.html',{'latest_question_list':latest_question_list})


def detail(request,question_id):
	r=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'q':r})
	
def results(request,question_id):
	q=get_object_or_404(Question,id=question_id)
	context={'q':q}
	return render(request,'polls/results.html',context)
#OLD VIEWS
'''