from django.db import models
from userPTK.models import UserPTK
from datetime import date

def get_current_date():
    return date.today()

class Stock(models.Model):
    """
    User stock, users can only have a single stock
    """
    user = models.OneToOneField(
        UserPTK,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"Stock from {self.user.name}"
    
class Product(models.Model):
    """
    Information of each products
    """
    EPOXY = 'EPO'
    TAPE = 'TAP'
    PUTTY = 'PUT'
    SILICONE = 'SIL'
    CYANOACRYLATE = 'CYA'
    GLUEPVCCPVC = 'GLU'
    PRODUCTS_TYPE_CHOICES = {
        EPOXY: 'Epoxy',
        TAPE: 'Tape',
        PUTTY: 'Putty',
        SILICONE: 'Silicone',
        CYANOACRYLATE: 'Cyanoacrylate',
        GLUEPVCCPVC: 'Glue PVC/CPVC'
    }
    
    name = models.CharField(max_length=50)
    product_type = models.CharField(
        max_length=3,
        choices=PRODUCTS_TYPE_CHOICES,
        default=EPOXY,
    )
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)   

    def __str__(self):
        return self.name
     
    
class ProductInStock(models.Model):
    """
    This model will be responsible for registering the products that enter and leave the stock.
    """
    inventary = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} of {self.inventary.user.name}"
    
class Rotation(models.Model):
    """
    This model will be responsible for registering the rotation of productos of Dealers
    """
    pending = models.BooleanField(default=True)
    date = models.DateField(default=get_current_date)
    user = models.ForeignKey(
        UserPTK,
        on_delete=models.CASCADE,
        null=True
    )
    
    def __str__(self):
        return f"{self.date} of {self.user.name}"
    
class ProductInRotation(models.Model):
    rotation = models.ForeignKey(
        Rotation,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    quantity = models.IntegerField(default=0)