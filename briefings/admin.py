from django.contrib import admin

from briefings import models


admin.site.register(models.Category)
admin.site.register(models.Briefing)
