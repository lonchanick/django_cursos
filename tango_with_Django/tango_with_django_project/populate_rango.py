def printDict(param):
	for dictt in param:
		for k,v in dictt.items():
			print('{0:5s}:{1}'.format(k,v))

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
	import random
	min,max=100,1000
	g=lambda min,max:random.randint(min,max) #genera un numero aleatorio entre 100 y 1000
	python_pages=[{'title':'Official Python Tutorial',
				   'url':'http://docs.python.org/3/tutorial/',
				   'views':g(min,max)},
				   {'title':'How to Think like a Computer Scientist',
				   'url':'http://www.greenteapress.com/thinkpython/',
				   'views':g(min,max)},
				   {'title':'Learn Python in 10 Minutes',
				   'url':'http://www.korokithakis.net/tutorials/python/',
				   'views':g(min,max)}]

	django_pages=[{'title':'Official Django Tutorial',
				   'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
				   'views':g(min,max)},
				   {'title':'Django Rocks',
				   'url':'http://www.djangorocks.com/',
				   'views':g(min,max)},
				   {'title':'How to Tango with Django',
				   'url':'http://www.tangowithdjango.com/',
				   'views':g(min,max)}]

	other_pages=[
				{'title':'Bottle','url':'http://bottlepy.org/docs/dev/','views':g(min,max)},
				{'title':'Flask','url':'http://flask.pocoo.org','views':g(min,max)},
				{'title':'Django Girls','url':'djangogirls.org','views':g(min,max)}]

	'''
	cat={'Python':{'page':python_pages},
		 'Django':{'page':django_pages},
		 'Other Frameworks':{'page':other_pages},}
	'''
	
	cat={'Python':[{'page':python_pages},128,64],
		 'Django':[{'page':django_pages},64,32],
		 'Other Frameworks':[{'page':other_pages},32,16]}		 

	for cat, cat_data in cat.items():
		c=add_cat(cat,cat_data[1],cat_data[2])
		for p in cat_data[0]['page']:
			add_page(c,p['title'],p['url'],p['views'])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print('- {0} - {1} - {2}'.format(str(c),str(p),p.views))

def add_page(cat,title,url,views=0):
	p=Page.objects.get_or_create(category=cat,title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name,views,likes):
	c=Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c

def main():
	print('Starting Rango population script...')
	populate()

	'''n,a='Irael','Arroyo'
				c={'datos':[n,a]}
				print(n,a)'''
	

	

if __name__ == '__main__':
	main()	

