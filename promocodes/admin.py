from django.contrib import admin
from promocodes.models import Promocode
# Register your models here.

@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ['pk' ,'listing', 'percentage_off', 'code', 'discounted_price']
