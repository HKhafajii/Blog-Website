from django import forms
from .models import User, Memory






class UserForm(forms.ModelForm):

    class Meta: 
        model = User
        fields = '__all__'

    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput(), max_length=50)
    # confirm_password = forms.CharField(widget= forms.PasswordInput(), max_length=50)

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = 'Title', 'content', 'image'

    Title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)

    

    

