from rest_framework.viewsets import ModelViewSet

from vendors import models
from vendors.serializers import VendorSerializer


class VendorViewSet(ModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = VendorSerializer
