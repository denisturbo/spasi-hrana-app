from django.db import models

from hranaapp.mixins import CreatedUpdatedAtMixin


# Create your models here.
class Order(CreatedUpdatedAtMixin, models.Model):
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)
    customer = models.ForeignKey('customauth.CustomerUser', on_delete=models.CASCADE)
    promocode = models.ForeignKey('promocodes.Promocode', null=True, blank=True, on_delete=models.CASCADE)