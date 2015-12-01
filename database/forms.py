__author__ = 'anjaneyulu'
from .models import *
from django import forms

class CompanyForm(forms.ModelForm):
    about = forms.CharField( widget=forms.Textarea )
    history = forms.CharField( widget=forms.Textarea )
    why_join = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Company
        exclude = []


class QuestionForm( forms.ModelForm ):

    data = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Question
        exclude = []
class ChoiceForm( forms.ModelForm ):

    description = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Choice
        exclude = []
class AnsForm( forms.ModelForm ):

    explination = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Choice
        exclude = []