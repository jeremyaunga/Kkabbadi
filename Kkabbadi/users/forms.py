from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('scorekeeper', 'Scorekeeper'), ('general_user', 'General User')])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label='Remember Me')
