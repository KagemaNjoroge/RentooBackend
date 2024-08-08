from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from Rentoo import settings

schema_view = get_schema_view(
    openapi.Info(
        title="RentooPMS API",
        default_version="v1",
        description="API for RentooPMS",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nyamburanjorogejames@students.uonbi.ac.ke"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # authentication
    path(
        "",
        include("authentication.urls"),
    ),
    # properties
    path(
        "",
        include("properties.urls"),
    ),
    # tenants
    path(
        "",
        include("tenants.urls"),
    ),
    # landlords
    path(
        "",
        include("landlords.urls"),
    ),
    # agents
    path(
        "",
        include("agents.urls"),
    ),
    # communication
    path(
        "",
        include("communication.urls"),
    ),
    # maintenance
    path(
        "",
        include("maintenance.urls"),
    ),
    # swagger docs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # jwt token
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # client
    path(
        "client/",
        include("client.urls"),
    ),
    # payments
    path(
        "",
        include("payments.urls"),
        name="payments",
    ),
    # company
    path(
        "",
        include("company.urls"),
        name="company",
    ),
    # utils => temporary files
    path(
        "",
        include("utils.urls"),
    ),
    # statistics
    path(
        "stats/",
        include("stats.urls"),
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
