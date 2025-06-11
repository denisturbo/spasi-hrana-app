from django.contrib import admin
from .models import Listing
# Register your models here
# 




@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin): #listings of businesses..
    list_display = ['pk' ,'connection', 'title', 'description', 'price']
