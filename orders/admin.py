from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['business', 'listing', 'customer', 'verification_code']
