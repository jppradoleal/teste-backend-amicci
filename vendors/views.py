from core.views import CreateRetrieveUpdateViewSet, ListViewSet
from vendors import models
from vendors.serializers import VendorSerializer


class VendorViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer


class ListVendorsViewSet(ListViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer
