# coding=utf-8
from django import forms
from website.models import Registration


class RegistrationForm(forms.ModelForm):
    files = forms.FileField(label='Pliki', required=True)
    checkbox_1 = forms.BooleanField(
        label="", required=True)
    checkbox_2 = forms.BooleanField(
        label="", required=True)

    class Meta:
        model = Registration
        exclude = ['pk']
