from django.urls import path

from .views import *
from .property import *
from .houses import *
from .agents import *
from .tenants import *

app_name = "client"

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    # property
    path("property/", property, name="property"),
    path("property/add/", new_property, name="new_property"),
    path("property/<int:id>/", property_details, name="property_details"),
    # houses
    path("houses/add/", new_house, name="new_house"),
    path("houses/<int:id>/", house_details, name="house_details"),
    path("houses/", houses, name="houses"),
    path("tenants/", tenants, name="tenants"),
    path("tenants/add/", new_tenant, name="new_tenant"),
    path("agents/add/", new_agent, name="new_agent"),
    path("agents/", agents, name="agents"),
    path("leases/", leases, name="leases"),
    path("reports/", reports, name="reports"),
    path("communication/", communication, name="communication"),
    path("landlords/", landlords, name="landlords"),
    path("maintenance/", maintenance, name="maintenance"),
    path("expenses/", expenses, name="expenses"),
    path("purchases/", purchases, name="purchases"),
    path("accounting/", accounting, name="accounting"),
    path("users/", users, name="users"),
    path("settings/", settings, name="settings"),
    path("subscription/", subscription, name="subscription"),
    path("cloud/", cloud, name="cloud"),
]
