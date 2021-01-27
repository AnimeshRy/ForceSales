from django import contrib
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Lead


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "test.html", context)


def detail_lead(request, pk):
    dLead = Lead.objects.get(id=pk)
    return render(request, "detail_lead.html", {
        "detail_lead": dLead
    })
