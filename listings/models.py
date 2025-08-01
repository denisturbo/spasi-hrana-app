from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from listings.choices import ListingStatus
from hranaapp.mixins import CreatedUpdatedAtMixin
from cloudinary_storage.storage import MediaCloudinaryStorage


# Create your models here.

class Listing(CreatedUpdatedAtMixin, models.Model):
    connection = models.ForeignKey('customauth.BusinessUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='listing_thumbs', storage=MediaCloudinaryStorage())
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.01,
                                            message='Сумата трябва да е над 0.01')])
    status = models.CharField(max_length=20, choices=ListingStatus.choices, default=ListingStatus.AVAILABLE)

    @property
    def eur_price(self) -> Decimal:
        return round(self.price / Decimal("1.95"), 2)

    def __str__(self):
        return self.title
