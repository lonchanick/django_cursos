from django.db import models

# Create your models here.
class Post(models.Model):
	topic=models.CharField(max_length=200)
	author=models.CharField(max_length=200)
	pub_date=models.DateTimeField('fecha de publicacion')

	def __str__(self):
		return self.topic

class Comment(models.Model):
	post=models.ForeignKey(Post, on_delete = models.CASCADE)
	comment_text=models.TextField()

	def __str__(self):
		return self.comment_text[0:50]

class Fields_types(models.Model):
	BIF=models.BigIntegerField() 


		