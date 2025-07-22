from django.db import models

from hranaapp.mixins import CreatedUpdatedAtMixin
import random
import string


# Create your models here.
class Order(CreatedUpdatedAtMixin, models.Model):
    business = models.ForeignKey('customauth.BusinessUser', on_delete=models.CASCADE)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)
    customer = models.ForeignKey('customauth.CustomerUser', on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=8, blank=True, null=True, editable=False,
                                         db_index=True)
    def create_verification_code(self):
        length = 8
        code = ''.join(random.choices(string.ascii_letters, k=length)).upper()
        return code

    def save(self, *args, **kwargs):
        if not self.verification_code:
            self.verification_code = self.create_verification_code()
        super().save(*args, **kwargs)
