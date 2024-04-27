from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Briefing(models.Model):
    name = models.CharField(max_length=255)
    retailer = models.ForeignKey("retailers.Retailer", on_delete=models.RESTRICT)
    responsible = models.ForeignKey("vendors.Vendor", on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    release_date = models.DateTimeField()
    available = models.BooleanField()

    def __str__(self) -> str:
        return self.name
