import requests

from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
from django.shortcuts import render, get_object_or_404


class InventoryList(generics.ListAPIView) : 
    queryset = Inventory.objects.select_related('supplier').all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name :
            qs = qs.filter(name__icontains=name)
        return qs


def inventory_list(request) :
    api_url = 'http://localhost:8000/api/inventory'
    response = requests.get(api_url)
    inventories = response.json() if response.status_code == 200 else []
    return render(request, 'inventory/list.html', {'inventories' : inventories})


def inventory_info(request, id) :
    item = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/info.html', {'item' : item})