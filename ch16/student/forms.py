from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# # Form validation 
#     def clean_email(self):
#         name_value = self.cleaned_data['name']
#         if len(name_value) < 10:
#             raise forms.ValidationError('Enter more than or equal to 10 characters.')
#         return name_value


# To validate everything
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if name_value and len(name_value) < 4:
            self.add_error('name', "Enter more than 4 characters.") 

        if email_value and len(email_value) < 20:
            self.add_error('email', "Enter more than 20 characters.") 

        return cleaned_data