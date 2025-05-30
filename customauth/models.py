from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from decimal import Decimal
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class BaseSpasiHranaUser(PermissionsMixin, AbstractBaseUser):

    class UserManager(BaseUserManager):
        def create_user(self, email, username, user_type, password=None, **extra_fields):
            if not email:
                raise ValueError("моля въвете email")
            email = self.normalize_email(email)
            user = self.model(email=email, username=username, user_type=user_type, **extra_fields)
            user.set_password(password)
            user.save()
            return user

        def create_superuser(self, email, username, user_type='customer', password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(email, username, user_type, password, **extra_fields)

    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('business', 'Business'),
    ]

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
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

        permissions = (
            ("can_create_listing", "Can Create Listing"),
            ("can_edit_listing", "Can Edit Listing"),
            ("can_delete_listing", "Can Delete Listing"),
            ("can_read_listing", "Can Read Listing"),
            ("can_order_listing", "Can Order Listing - deletes order from Client to Business Side"),
        )



class BusinessUser(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('sushi', 'Sushi'),
        ('coffee', 'Coffee'),
        ('buffet', 'Buffet'),
        ('doner', 'Doner'),
        ('other', 'Other'),

    ]

    user = models.OneToOneField(BaseSpasiHranaUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    business_type = models.CharField(max_length=10, choices=BUSINESS_TYPE_CHOICES)


    def __str__(self):

        return self.business_name

class CustomerUser(models.Model):
    user = models.OneToOneField(BaseSpasiHranaUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Listing(models.Model):
    connection = models.ForeignKey(BusinessUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01, message='Сумата трябва да е над 0.01')])

    def eur_price(self) -> Decimal:
        return round(self.price / Decimal("1.95"), 2)
    

