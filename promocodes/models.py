from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class Promocode(models.Model):
    connection = models.ForeignKey('customauth.BusinessUser', on_delete=models.CASCADE)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)
    percentage_off = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    code = models.CharField(max_length=10, unique=True)

    def discounted_price(self) -> Decimal:
        original_price = self.listing.price
        discount = original_price * (Decimal(self.percentage_off) / Decimal(100))
        return round((original_price - discount),2)