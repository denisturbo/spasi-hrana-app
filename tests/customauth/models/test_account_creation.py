from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth import get_user_model
from customauth.choices import BusinessTypeChoices, UserTypeChoices
from customauth.models import BusinessUser


UserModel = get_user_model()


class TestAccountCreation(TestCase):
    def setUp(self):
        self.username = "user"
        self.email = "email@email.bg"
        self.user_type = UserTypeChoices.BUSINESS
        self.phone_number = '0878475149'
        self.password = "banitsa1"
        self.data = {
            "username": self.username,
            "email": self.email,
            "user_type": self.user_type,
            "phone_number": self.phone_number,
            "password": self.password,
        }

        self.business_data = {
        "business_name": "Burger1",
        "location": "Sofia",
        "profile_picture": "image.jpg",
        "business_type": BusinessTypeChoices.FAST_FOOD
        }
        self.base_user = UserModel.objects.create_user(**self.data)
        self.business_user = BusinessUser.objects.create(user=self.base_user,
                                                         **self.business_data)
    def test__valid_return_of_email_base(self):
        self.assertEqual(self.email, str(self.base_user))

    def test__valid_return_of_business_name(self):
        self.assertEqual('Burger1', str(self.business_user))

    def test__same_username__raise_integrity_error(self):
        self.data['email'] = 'kk@kk.bg'
        with self.assertRaises(IntegrityError) as ie:
            UserModel.objects.create_user(**self.data)
        self.assertIn("UNIQUE constraint", str(ie.exception))

    def test__invalid_phone_number_expect_success(self):
        self.data['phone_number'] = '123'
        self.data['email'] = 'kk@kk.bg'
        self.data['username'] = 'bobo'
        test = UserModel.objects.create_user(**self.data)
        with self.assertRaises(ValidationError):
            test.full_clean()

    def test_valid_phone_number_expect_success(self):
        self.data['phone_number'] = '0878475149'
        self.data['email'] = 'kk@kk.bg'
        self.data['username'] = 'bobo'
        test = UserModel.objects.create_user(**self.data)
        test.full_clean()