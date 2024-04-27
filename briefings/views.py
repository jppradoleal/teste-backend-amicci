from rest_framework.viewsets import ModelViewSet

from briefings import models
from briefings.serializers import BriefingSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class BriefingViewSet(ModelViewSet):
    queryset = models.Briefing.objects.all()
    serializer_class = BriefingSerializer
