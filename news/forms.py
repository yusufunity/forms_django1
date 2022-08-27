from django import forms

from .models import Category

###------ModeleForm,Form

class NewsForm(forms.Form):
	
	title=forms.CharField(max_length=150)
	content=forms.CharField()
	is_published=forms.BooleanField()	
	### queryset parametri
	category=forms.ModelChoiceField(queryset=Category.objects.all())

