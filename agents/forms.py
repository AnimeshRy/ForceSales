from django import forms
from django.contrib.auth import models
from django.forms import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# get user model
User = get_user_model()


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )
