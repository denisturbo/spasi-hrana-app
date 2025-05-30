from django.contrib import admin
from .models import BaseSpasiHranaUser, BusinessUser, Listing, CustomerUser
# Register your models here.
@admin.register(BaseSpasiHranaUser)
class BaseUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type']


@admin.register(BusinessUser)
class BusinessUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'business_type']

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']



@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['pk' ,'connection', 'title', 'description', 'price']

