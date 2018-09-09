from django import forms
from .models import Condition

class ConditionForm(forms.ModelForm):

	class Meta:
		model = Condition
		fields = '__all__'

class CityForm(forms.Form):
	city = forms.CharField(required=True)
