from briefings import models
from core.serializers import ModelSerializerWithOwner


class CategorySerializer(ModelSerializerWithOwner):
    class Meta:
        model = models.Category
        fields = ["id", "name", "description", "owner"]
        read_only_fields = ["id", "owner"]


class BriefingSerializer(ModelSerializerWithOwner):
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
            "owner",
        ]

        read_only_fields = ["id", "owner"]
