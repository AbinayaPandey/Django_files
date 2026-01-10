from django import forms


class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    city = forms.CharField()
