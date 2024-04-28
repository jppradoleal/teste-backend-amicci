from core.serializers import ModelSerializerWithOwner
from vendors import models


class VendorSerializer(ModelSerializerWithOwner):
    class Meta:
        model = models.Vendor
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]
