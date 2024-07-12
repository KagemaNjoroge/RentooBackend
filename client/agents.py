from agents.models import Agent
from django.shortcuts import render
from properties.models import Property


def agents(request):
    data = Agent.objects.all()
    return render(
        request,
        "agents/index.html",
        context={"agents": data},
    )


def new_agent(request):
    property = Property.objects.all()
    return render(
        request,
        "agents/new.html",
        {"properties": property},
    )
