from django.db import models 

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('fecha de publicación',auto_now=True)

	def __str__(self):
		return "{}".format(self.question_text)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	update_date = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return "{} -> {}".format(self.choice_text,self.question.question_text)

