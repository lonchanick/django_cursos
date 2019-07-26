from django import forms

class PreguntaForm(forms.Form): 
	pregunta = forms.CharField(max_length=200, required=True)
