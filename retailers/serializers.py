from rest_framework.serializers import ModelSerializer

from retailers import models

class RetailerSerializer(ModelSerializer):
    class meta:
        model = models.Retailer
        fields = ['id', 'name']
        read_only_fields = ['id']
