from django.db import models

from amicci import settings


class Retailer(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True)

    def __str__(self) -> str:
        return self.name
