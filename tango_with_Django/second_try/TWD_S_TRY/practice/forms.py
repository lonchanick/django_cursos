from django import forms
from practice.models import Fields_types

class Fields_types_form(forms.ModelForm):
	BIF=forms.IntegerField(help_text='Big Integer Field')

	class Meta:
		model=Fields_types
		fields=('BIF',)
				