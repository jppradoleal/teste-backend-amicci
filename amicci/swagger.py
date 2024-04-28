from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Amicci Demo",
        description="Essa API tem o objetivo de avaliar potenciais candidatos",
        default_version="1.0.0",
        contact=openapi.Contact(
            name="João Pedro Prado Leal",
            email="joaopedro0128@hotmail.com"
        )
    ),
    public=True,
    permission_classes=(IsAuthenticatedOrReadOnly,)
)
