from rest_framework.permissions import IsAuthenticatedOrReadOnly

from briefings import models
from briefings.serializers import BriefingSerializer, CategorySerializer
from core.permissions import IsOwnerOrReadOnly
from core.views import CreateRetrieveUpdateViewSet, ListViewSet


class CategoryViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ListCategoriesViewSet(ListViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class BriefingViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ListBriefingsViewSet(ListViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
