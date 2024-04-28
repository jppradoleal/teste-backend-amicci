from rest_framework.serializers import ModelSerializer

from briefings import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "name", "description"]
        read_only_fields = ["id"]


class BriefingSerializer(ModelSerializer):
    class Meta:
        model = models.Briefing
        fields = [
            "id",
            "name",
            "retailer",
            "responsible",
            "category",
            "release_date",
            "available",
        ]

        read_only_fields = ["id"]
