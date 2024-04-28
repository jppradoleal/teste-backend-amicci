from core.views import CreateRetrieveUpdateViewSet, ListViewSet
from retailers import models
from retailers.serializers import RetailerSerializer


class RetailerViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Retailer.objects.all().prefetch_related("briefing_set")
    serializer_class = RetailerSerializer


class ListRetailersViewSet(ListViewSet):
    queryset = models.Retailer.objects.all().prefetch_related("briefing_set")
    serializer_class = RetailerSerializer
