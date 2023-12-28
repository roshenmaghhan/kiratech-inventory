from typing import Any, Optional
from django.core.management.base import BaseCommand
from inventory.models import Supplier, Inventory

import random

class Command(BaseCommand) :
    help = "Generates dummy data, to be populated in the database"

    def handle(self, *args, **kwargs) :

        # Creates 5 suppliers, in the suppliers table
        for i in ['Alibaba', 'Dover', 'Crove', 'Megagoods', 'SaleHoo'] :
            Supplier.objects.create(name=i)
        
        suppliers_list = Supplier.objects.all()

        dummy_names = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"

        for i in dummy_names.split(" ") :
            Inventory.objects.create(
                name=i,
                description='A generic product description.',
                note='A generic note, of this product.',
                stock=random.randint(1, 100),
                availability=True,
                supplier=random.choice(suppliers_list)
            )

        print("Successfully Generated Dummy Data.")