from rest_framework.serializers import ModelSerializer

from vendors import models


class VendorSerializer(ModelSerializer):
    class meta:
        model = models.Vendor
        fields = ["id", "name"]
        read_only_fields = ["id"]
