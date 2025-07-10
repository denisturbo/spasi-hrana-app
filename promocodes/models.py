from typing import Any

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

from hranaapp.mixins import CreatedUpdatedAtMixin


# Create your models here.

class Promocode(CreatedUpdatedAtMixin, models.Model):
    connection = models.ForeignKey('customauth.BusinessUser', on_delete=models.CASCADE)
    listing = models.ManyToManyField('listings.Listing')
    percentage_off = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    code = models.CharField(max_length=10, unique=True)

    def discounted_price(self) -> dict[Any, Any]:
        discounted = {}
        for item in self.listing.all():
            print(item)
            original_price = item.price
            discount = original_price * (Decimal(self.percentage_off) / Decimal(100))
            discounted[item.id] = round((original_price - discount),2)
        return discounted

    def __str__(self):
        return self.listing
