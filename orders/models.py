from django.db import models

from hranaapp.mixins import CreatedUpdatedAtMixin


# Create your models here.
class Order(CreatedUpdatedAtMixin):
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)
    customer = models.ForeignKey('customauth.CustomerUser', on_delete=models.CASCADE)
