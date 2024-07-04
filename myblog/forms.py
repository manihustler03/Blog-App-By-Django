from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
                'class': 'form-control'
            })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
                'class': 'form-control'
            })

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),required=False)
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}),required=False)
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),required=False, label='Enter Your Password')
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),required=False,label='Enter Your Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
