from django.shortcuts import render,redirect
from django.http import HttpResponse
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm
from django.urls import reverse

def index(request):
	categoy_list=Category.objects.order_by('-likes')[:5]
	five_most_viewed_pages=Page.objects.order_by('-views')[:3]
	context_dict={}
	context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
	context_dict['categories']=categoy_list
	context_dict['five_most_viewed_pages']=five_most_viewed_pages

	return render(request,'rango/index.html',context_dict)

def about(request):
	context_dict={'boldmessage':'This is "about.html" page'}
	return render(request,'rango/about.html',context=context_dict)

def israel(request):
	return render(request,'rango/israel.html',{})

def show_category(request,category_name_slug):
	context_dict={}
	try:
		category=Category.objects.get(slug=category_name_slug)
		pages=Page.objects.filter(category=category)
		context_dict['pages']=pages
		context_dict['category']=category

	except Category.DoesNotExist:
		context_dict['category']=None
		context_dict['pages']=None

	return render(request,'rango/category.html',context_dict)

def add_category(request):
	form=CategoryForm()

	if request.method == 'POST':
		form=CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request,'rango/add_category.html',{'form':form})

def add_page(request,category_name_slug):
	try:
		category=Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category=None

	form=PageForm()
	if request.method == 'POST':
		form=PageForm(request.POST)
		if form.is_valid():
			if category:
				page=form.save(commit=False)
				page.category=category
				page.views=0
				page.save()
				return redirect(reverse('rango:show_category',
										kwargs={'category_name_slug':category_name_slug}))
		else:
			print(form.errors)

	context_dict={'form':form,'category':category}		
	return render(request,'rango/add_page.html',context_dict)