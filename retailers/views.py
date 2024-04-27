from core.views import CreateListRetrieveUpdateViewSet
from retailers import models
from retailers.serializers import RetailerSerializer


class RetailerViewSet(CreateListRetrieveUpdateViewSet):
    queryset = models.Retailer.objects.all()
    serializer_class = RetailerSerializer
