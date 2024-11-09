from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': '',
        'class': 'my-input'
    }))

def __init__(self, *args, **kwargs):
    super(RegistrationForm, self).__init__(*args, **kwargs)
    self.fields['password1'].widget.attrs.update({
        'placeholder': "Введите пароль",
        'class': "my-input"
    })
    self.fields['password2'].widget.attrs.update({
        'placeholder': "Повторите пароль",
        'class': "my-input"
    })

    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Введите имя пользователя", 'class': "my-input"}),
        }