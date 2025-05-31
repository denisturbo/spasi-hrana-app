from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from customauth.models import BusinessUser
# Create your models here.

class Listing(models.Model):
    connection = models.ForeignKey(BusinessUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01, message='Сумата трябва да е над 0.01')])

    created_on = models.DateTimeField(auto_now_add=True)

    def eur_price(self) -> Decimal:
        return round(self.price / Decimal("1.95"), 2)
    

