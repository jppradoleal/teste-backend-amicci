from rest_framework import serializers

from retailers import models
from vendors.models import Vendor
from vendors.serializers import VendorSerializer


class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.SerializerMethodField()

    class Meta:
        model = models.Retailer
        fields = ["id", "name", "vendors"]
        read_only_fields = ["id", "vendors"]

    def get_vendors(self, obj):
        briefings = obj.briefing_set.all()
        vendor_ids = briefings.values_list("responsible", flat=True).distinct()
        vendors = Vendor.objects.filter(id__in=vendor_ids)
        return VendorSerializer(vendors, many=True).data
