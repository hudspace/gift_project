from django.contrib import admin

from . import models


class RecipientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['first_name']

class GiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'purchased']

admin.site.register(models.Recipient, RecipientAdmin)
admin.site.register(models.Gift, GiftAdmin)
