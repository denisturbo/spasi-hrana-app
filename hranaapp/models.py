from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2) # Valuta BGN
    
