from django.db import models

# Supplier model class
class Supplier(models.Model) : 
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name

# Inventory model class
class Inventory(models.Model) : 
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self) : 
        return self.name