from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm
from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

