from django.shortcuts import render
from tenants.models import Tenant
from properties.models import Property


def tenants(request):
    data = Tenant.objects.all()
    return render(
        request,
        "tenants/index.html",
        context={"tenants": data},
    )


def new_tenant(request):

    return render(
        request,
        "tenants/new.html",
    )
