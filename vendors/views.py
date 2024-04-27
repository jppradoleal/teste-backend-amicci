from core.views import CreateListRetrieveUpdateViewSet
from vendors import models
from vendors.serializers import VendorSerializer


class VendorViewSet(CreateListRetrieveUpdateViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer
