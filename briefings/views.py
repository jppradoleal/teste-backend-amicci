from briefings import models
from briefings.serializers import BriefingSerializer, CategorySerializer
from core.views import CreateRetrieveUpdateViewSet, ListViewSet


class CategoryViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class ListCategoriesViewSet(ListViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class BriefingViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer


class ListBriefingsViewSet(ListViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer
