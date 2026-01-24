from django import forms 


class Registration(forms.Form):
    name = forms.CharField(max_length=50, error_messages={'required': "Name is required."})
    email = forms.EmailField(error_messages={"required": "Email is required."})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={"required": "Password is required."})


# To validate everything
def clean(self):
    cleaned_data = super().clean()
    name_value = cleaned_data.get("name")
    email_value = cleaned_data.get("email")

    if name_value and len(name_value) < 4:
        self.add_error("name", "Enter more than 4 characters.")

    if email_value and len(email_value) < 20:
        self.add_error("email", "Enter more than 20 characters.")

    return cleaned_data
