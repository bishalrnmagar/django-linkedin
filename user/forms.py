from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget = forms.HiddenInput()
        self.fields['password2'].label = ''

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password2'] = cleaned_data['password1']
        return cleaned_data
