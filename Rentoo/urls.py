from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Rentoo API",
        default_version="v1",
        description="API for Rentoo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nyamburanjorogejames@students.uonbi.ac.ke"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    # properties
    path("properties/", include("properties.urls")),
    # tenants
    path("tenants/", include("tenants.urls")),
    # landlords
    path("landlords/", include("landlords.urls")),
    # agents
    path("agents/", include("agents.urls")),
    # communication
    path("communication/", include("communication.urls")),
    # maintenance
    path("maintenance/", include("maintenance.urls")),
    # swagger docs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # jwt token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
