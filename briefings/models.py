from django.db import models

from amicci import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True)

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True)

    def __str__(self) -> str:
        return self.name
