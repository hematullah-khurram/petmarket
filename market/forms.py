from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pet

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'color', 'description', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
