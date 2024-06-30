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
    # admin
    path("admin/", admin.site.urls),
    # authentication
    path("api/auth/", include("authentication.urls")),
    # properties
    path("api/properties/", include("properties.urls")),
    # tenants
    path("api/tenants/", include("tenants.urls")),
    # landlords
    path("api/landlords/", include("landlords.urls")),
    # agents
    path("api/agents/", include("agents.urls")),
    # communication
    path("api/communication/", include("communication.urls")),
    # maintenance
    path("api/maintenance/", include("maintenance.urls")),
    # swagger docs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # jwt token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # client
    path("", include("client.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
