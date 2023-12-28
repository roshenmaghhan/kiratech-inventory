from django.urls import reverse
from django.test import TestCase
from .models import Inventory, Supplier

class InventoryTestCase(TestCase) :
    
    def setUp(self) :
        supplier = Supplier.objects.create(name="Test Supplier")
        Inventory.objects.create(
            name='Dummy Item',
            description='Dummy Description',
            note='Dummy Note',
            stock=5,
            availability=True,
            supplier=supplier
        )

    def test_inventory_list(self) :
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_info(self) :
        item = Inventory.objects.first()
        response = self.client.get(reverse('inventory_info', args=[item.id]))
        self.assertEqual(response.status_code, 200)

    def test_inventory_api(self) :
        response = self.client.get(reverse('api_inventory'))
        self.assertEqual(response.status_code, 200)