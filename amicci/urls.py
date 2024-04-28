from django.contrib import admin
from django.urls import path, include
from amicci.swagger import schema_view

swagger_urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns = swagger_urlpatterns + [
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration", include("dj_rest_auth.registration.urls")),
    path("", include("vendors.urls")),
    path("", include("retailers.urls")),
    path("", include("briefings.urls")),
]
