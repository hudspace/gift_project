from django.contrib import admin

from . import models

admin.site.register(models.Recipient)
admin.site.register(models.Gift)
