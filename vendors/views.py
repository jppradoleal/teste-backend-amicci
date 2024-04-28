from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import IsOwnerOrReadOnly
from core.views import CreateRetrieveUpdateViewSet, ListViewSet
from vendors import models
from vendors.serializers import VendorSerializer


class VendorViewSet(CreateRetrieveUpdateViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ListVendorsViewSet(ListViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
