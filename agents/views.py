from django.contrib import auth
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail
import random


class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"

    # only return agents with the request.user organization
    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)


class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(0,100000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent to the CRM, please come and start working",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        # agent.organization = self.request.user.userprofile
        # agent.save()
        return super().form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

    def get_success_url(self):
        return reverse("agents:agent_list")


class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

    def get_success_url(self) -> str:
        return reverse("agents:agent_list")
