from django import forms
from rango.models import Page, Category

ml=128 #max length de campo char field

class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=ml,help_text='Please enter the category')
	views=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug=forms.CharField(widget=forms.HiddenInput,required=False)

	class Meta:
		model=Category
		fields=('name',)

class PageForm(forms.ModelForm):
	title=forms.CharField(max_length=ml,help_text='Enter the title page')
	url=forms.URLField(max_length=200,help_text='enter the URL')
	views=forms.IntegerField(widget=forms.HiddenInput, initial=0)

	class Meta:
		model=Page
		exclude=('category',)

			



