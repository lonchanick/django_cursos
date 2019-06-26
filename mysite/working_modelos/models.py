from django.db import models

# Create your models here.
class User(models.Model):
	GENDERS = [('Male','Male'), ('Female','Female')]
	#Lista de generos
	first_name = models.CharField("Primer nombre", max_length=50, default ="Pepe Clabo")
	last_name = models.CharField("Segundo nombre", max_length=50)
	email = models.EmailField("Campo Email", max_length = 50)
	nickname = models.CharField(max_length=50)
	password = models.CharField(max_length = 50)
	age = models.DateField()
	sex = models.CharField(max_length=1, choices = GENDERS, help_text =" Choose your gender!")
	date_reg = models.DateField(auto_now_add = True)
	#esto "auto_now_add = True" guarda la fecha de creacion del registro
	profile_picture = models.ImageField(upload_to = "static/working_modelos/images/profile")


	"""	
	first_name
	last_name
	email
	nickname
	password
	age
	sex
	date_reg #fecha de registro (se guarda al crear un nuevo usuario)
	profile_picture
	"""