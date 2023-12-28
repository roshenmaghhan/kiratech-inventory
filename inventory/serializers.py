from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer) : 
    supplier_name = serializers.CharField(source='supplier.name')

    class Meta : 
        model = Inventory
        fields = ['name', 'supplier_name', 'availability']