from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length = 200)
	passw = models.CharField(max_length = 20)
	nickname = models.CharField(max_length = 20)
	fecha_reg = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "Nombre: {} - Passw: {} - Nickname {}".format(
			self.nombre, self.passw, self.nickname)

class Pregunta(models.Model):
	usuario = models.ForeignKey (Usuario, on_delete = models.CASCADE)
	texto = models.CharField(max_length = 200)

	def __str__(self):
		return "->{}".format(self.texto)

class Owner(models.Model):
    nombre = models.CharField(max_length = 200,default="default_name")

class Item(models.Model):
    owner = models.ForeignKey(Owner, related_name='items', on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 200,default="default_name")
		

		