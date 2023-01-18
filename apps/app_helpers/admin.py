from django.contrib import admin

from apps.app_helpers.models import Inventory, PhoneCode

admin.site.register(PhoneCode)
admin.site.register(Inventory)
