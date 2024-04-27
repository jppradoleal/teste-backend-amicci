from briefings import models
from briefings.serializers import BriefingSerializer, CategorySerializer
from core.views import CreateListRetrieveUpdateViewSet


class CategoryViewSet(CreateListRetrieveUpdateViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class BriefingViewSet(CreateListRetrieveUpdateViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer
