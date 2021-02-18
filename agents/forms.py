from django import forms
from django.contrib.auth.forms import UserCreationForm
from leads.models import User, Agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
