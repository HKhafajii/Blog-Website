from django import forms
from .models import User






class UserForm(forms.ModelForm):

    class Meta: 
        model = User
        fields = '__all__'

    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput(), max_length=50)
    # confirm_password = forms.CharField(widget= forms.PasswordInput(), max_length=50)

    

    

