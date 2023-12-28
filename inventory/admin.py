from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryManager(admin.ModelAdmin) :
    list_display = ('name', 'description', 'stock', 'availability', 'supplier')
    search_fields = ('name', 'supplier__name')