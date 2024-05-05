from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput(), max_length=50)
    username = forms.CharField(max_length=50)

