from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.contrib import admin
from django.urls import include, path

from amicci.swagger import schema_view

swagger_urls = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

auth_urls = [
    path("auth/login/", LoginView.as_view(), name="user-login"),
    path("auth/logout/", LogoutView.as_view(), name="user-logout"),
    path("auth/register/", RegisterView.as_view(), name="user-register"),
    path("auth/user/", UserDetailsView.as_view(), name="user-details"),
]

urlpatterns = (
    swagger_urls
    + auth_urls
    + [
        path("admin/", admin.site.urls),
        path("", include("vendors.urls")),
        path("", include("retailers.urls")),
        path("", include("briefings.urls")),
    ]
)
