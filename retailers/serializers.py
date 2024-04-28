from rest_framework import serializers

from core.serializers import ModelSerializerWithOwner
from retailers import models
from vendors.models import Vendor
from vendors.serializers import VendorSerializer


class RetailerSerializer(ModelSerializerWithOwner):
    vendors = serializers.SerializerMethodField()

    class Meta:
        model = models.Retailer
        fields = ["id", "name", "vendors", "owner"]
        read_only_fields = ["id", "vendors", "owner"]

    def get_vendors(self, obj):
        briefings = obj.briefing_set.all()
        vendor_ids = briefings.values_list("responsible", flat=True).distinct()
        vendors = Vendor.objects.filter(id__in=vendor_ids)
        return VendorSerializer(vendors, many=True).data
