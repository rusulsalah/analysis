

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)

    def clean(self):
        data=self.cleaned_data

        username =data.get('username')
        password =data.get('password')
        return data


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    first_name = forms.CharField(max_length=100, label= 'First Name :')
    last_name = forms.CharField(max_length=100, label= 'last Name :')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )


