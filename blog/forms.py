from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            "title": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название поста'
            }),
            "text": forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст статьи'
            })
        }

class SignUp(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            "username": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
            }),
            "email": forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
            }),
        }
