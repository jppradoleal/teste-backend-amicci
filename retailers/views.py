from core.views import CreateListRetrieveUpdateViewSet
from retailers import models
from retailers.serializers import RetailerSerializer


class RetailerViewSet(CreateListRetrieveUpdateViewSet):
    queryset = models.Retailer.objects.all().prefetch_related('briefing_set')
    serializer_class = RetailerSerializer
