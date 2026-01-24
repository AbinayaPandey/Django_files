from django import forms


class Registration(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# This file runs after views.py as it specifies form described here.
