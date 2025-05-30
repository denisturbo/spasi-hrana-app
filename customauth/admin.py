from django.contrib import admin
from .models import BaseSpasiHranaUser, BusinessUser, Listing, CustomerUser

@admin.register(BaseSpasiHranaUser) # All users
class BaseUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type'] 
    list_filter = ['is_active']

@admin.register(BusinessUser)
class BusinessUserAdmin(admin.ModelAdmin): #Business only
    list_display = ['user', 'business_name', 'business_type']

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin): #Customers only
    list_display = ['user', 'first_name', 'last_name']



@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin): #listings of businesses..
    list_display = ['pk' ,'connection', 'title', 'description', 'price']

