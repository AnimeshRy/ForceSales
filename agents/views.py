from django.contrib import auth
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"

    # only return agents with the request.user organization
    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super().form_valid(form)


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

    def get_success_url(self):
        return reverse("agents:agent_list")


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_organization)

    def get_success_url(self) -> str:
        return reverse("agents:agent_list")
