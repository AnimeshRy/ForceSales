from django import forms
# from django.contrib.auth import get_user_model
from .models import Lead, User, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField

# User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", ]
        field_classes = {
            'username': UsernameField
        }


class AssignAgentForm(forms.Form):
    # assign empty queryset and then dynamically update it
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
