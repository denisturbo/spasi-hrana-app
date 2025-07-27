from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from customauth.choices import BusinessTypeChoices, UserTypeChoices
from customauth.models import BusinessUser
from listings.choices import ListingStatus
from listings.models import Listing

UserModel = get_user_model()


class TestListingreation(TestCase):
    def setUp(self):
        self.base_user_creds = {
            "username": "ivan1",
            "email":"ivan1@abv.bg",
            "user_type":UserTypeChoices.BUSINESS,
            "phone_number":"0878475999",
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

        self.listing = Listing.objects.create(
            connection = self.business_user,
            title = "KFC 1",
            description = "baba",
            image = "image.png",
            price = Decimal(10.00)
        )


    def test_returning_of_string_expect_success(self):
        self.assertEqual(self.listing.title, str(self.listing))


    def test_default_status_is_available(self):
        self.assertEqual(self.listing.status, ListingStatus.AVAILABLE)

    def test_listing_price_negative(self):
        self.listing.price = Decimal("-5.00")
        with self.assertRaises(ValidationError):
            self.listing.full_clean()
