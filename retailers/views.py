from rest_framework.viewsets import ModelViewSet

from retailers import models
from retailers.serializers import RetailerSerializer


class RetailerViewSet(ModelViewSet):
    queryset = models.Retailer.objects.all()
    serializer_class = RetailerSerializer
