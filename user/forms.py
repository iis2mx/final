from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    username = forms.CharField()
    username.widget.attrs.update({'class': 'form-content'})
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()




    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
