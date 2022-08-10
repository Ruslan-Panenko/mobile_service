from django import forms

from apps.service.models import Phone


class CreateTask(forms.Form):
    brand = forms.CharField(max_length=255)
    problem = forms.CharField(widget=forms.Textarea)


class CreateInvoice(forms.Form):
    description = forms.CharField(max_length=255, widget=forms.Textarea)
    price = forms.FloatField()
