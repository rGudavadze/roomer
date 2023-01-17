from django.contrib import admin

from apps.shared.models import Inventory, PhoneCode

admin.site.register(PhoneCode)
admin.site.register(Inventory)
