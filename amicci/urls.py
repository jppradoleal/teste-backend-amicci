from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration", include("dj_rest_auth.registration.urls")),
    path("vendors/", include("vendors.urls")),
    path("retailers/", include("retailers.urls")),
    path("", include("briefings.urls")),
]
