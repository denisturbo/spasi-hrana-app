from django.db import models

class BusinessTypeChoices(models.TextChoices):
    COFFEE = 'coffee', 'Coffee'
    RESTAURANT = 'restaurant', 'Restaurant'
    FAST_FOOD = 'fast_food', 'Fast Food'
    OTHER = 'other', 'Other'

class UserTypeChoices(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    BUSINESS = 'business', 'Business'