from django.contrib import admin

from apps.rooms.models import Inventory, Room

admin.site.register(Room)
admin.site.register(Inventory)
