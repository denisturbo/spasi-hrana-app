from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from customauth.choices import BusinessTypeChoices, UserTypeChoices
from customauth.managers import UserManager
from customauth.validators import BulgarianPhoneNumberValidator
from hranaapp.mixins import CreatedUpdatedAtMixin


# Create your models here.

class BaseSpasiHranaUser(PermissionsMixin, AbstractBaseUser):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=UserTypeChoices.choices)
    phone_number = models.CharField(max_length=13, validators=[BulgarianPhoneNumberValidator()])



    is_active = models.BooleanField(default=True) # True for Client.. can be turned OFF/False for Business (manaul approval)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username', 'user_type']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "All User"
        verbose_name_plural = "All users"


class BusinessUser(CreatedUpdatedAtMixin, models.Model):


    user = models.OneToOneField(BaseSpasiHranaUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='pfps', null=True, blank=True,  storage=MediaCloudinaryStorage())
    business_type = models.CharField(max_length=10, choices=BusinessTypeChoices.choices)

    def __str__(self):
        return self.business_name
    
    class Meta:
        permissions = (
            ("can_create_listing", "Can Create Listing"),
            ("can_edit_listing", "Can Edit Listing"),
            ("can_delete_listing", "Can Delete Listing"),
            ("can_read_listing", "Can Read Listing"),
        )

class CustomerUser(CreatedUpdatedAtMixin, models.Model):
    user = models.OneToOneField(BaseSpasiHranaUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:    
        permissions = (
            ("can_order_listing", "Can Order Listing - deletes order from Client to Business Side"),
        )