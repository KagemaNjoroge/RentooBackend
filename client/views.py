from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def login(request):
    return render(request, "auth/login.html")


def tenants(request):
    return render(request, "tenants/index.html")


def agents(request):
    return render(request, "agents/index.html")


def leases(request):
    return render(request, "leases/index.html")


def reports(request):
    return render(request, "reports/index.html")


def communication(request):
    return render(request, "communication/index.html")


def landlords(request):
    return render(request, "landlords/index.html")


def maintenance(request):
    return render(request, "maintenance/index.html")


def expenses(request):
    return render(request, "expenses/index.html")


def purchases(request):
    return render(request, "purchases/index.html")


def accounting(request):
    return render(request, "accounting/index.html")


def users(request):
    return render(request, "users/index.html")


def settings(request):
    return render(request, "settings/index.html")


def subscription(request):
    return render(request, "subscription/index.html")


def cloud(request):
    return render(request, "cloud/index.html")
