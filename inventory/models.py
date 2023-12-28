from django.db import models
from django.core.validators import MinValueValidator

# Supplier model class
class Supplier(models.Model) : 
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self) :
        return self.name

# Inventory model class
class Inventory(models.Model) : 
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    note = models.TextField() # Note should be optional
    stock = models.IntegerField(validators=[MinValueValidator(0)]) # Stock shouldn't be a negative number (?)
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self) : 
        return self.name