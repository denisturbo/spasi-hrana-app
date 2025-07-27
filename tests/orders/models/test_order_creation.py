from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from customauth.choices import BusinessTypeChoices, UserTypeChoices
from customauth.models import BusinessUser, CustomerUser
from listings.choices import ListingStatus
from listings.models import Listing
from orders.models import Order

UserModel = get_user_model()


class TestOrderCreation(TestCase):
    def setUp(self):
        self.base_user_creds = {
            "username": "ivan1",
            "email":"ivan1@abv.bg",
            "user_type":UserTypeChoices.BUSINESS,
            "phone_number":"0878475999",
            "password": "Trudna123!"
        }
        self.base_user_business = UserModel.objects.create_user(**self.base_user_creds)

        self.business_creds = {
            "user": self.base_user_business,
            "business_name": "KFC",
            "location": "Sofia",
            "profile_picture": "image.png",
            "business_type": BusinessTypeChoices.COFFEE,

        }

        self.business_user = BusinessUser.objects.create(**self.business_creds)

        self.base_user_creds["user_type"] = UserTypeChoices.CUSTOMER
        self.base_user_creds['username'] = 'CLIENT1'
        self.base_user_creds['email'] = 'client1@abv.bg'

        self.base_user_customer = UserModel.objects.create_user(**self.base_user_creds)

        self.client_creds = {
            "user": self.base_user_customer,
            "first_name": "Ivan",
            "last_name": "Petrov"
        }

        self.customer_user = CustomerUser.objects.create(**self.client_creds)

        self.listing = Listing.objects.create(
            connection = self.business_user,
            title = "KFC 1",
            description = "baba",
            image = "image.png",
            price = Decimal(10.00),
            status = ListingStatus.AVAILABLE
        )

    def test_create_order_successfully(self):
        self.client.login(email="client1@abv.bg", password="Trudna123!")
        response = self.client.post(
            reverse('orders:create', kwargs={"pk": self.listing.pk})
        )
        self.listing.refresh_from_db()
        order = Order.objects.first()

        # Assertions
        self.assertEqual(order.listing, self.listing)
        self.assertEqual(self.listing.status, ListingStatus.ORDERED)


