from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SelectAlgorithm():
    ALGO_CHOICES= [
    ('CAG', 'Classic Genetic Algorithm'),
    ('DE', 'Differential Evolution'),
    ('BCA', 'Bee Colony Algorithm'),
    ]
    algorithm = forms.ChoiceField(label='What algorithm do you want to try?',
                                  widget=forms.RadioSelect,
                                  choices=ALGO_CHOICES)