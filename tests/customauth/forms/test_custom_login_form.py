from django.test import TestCase
from customauth.forms import CustomLoginForm

class TestCustomLoginForm(TestCase):
    def setUp(self):
        self.data = {
            'username': "fake@email.bg",
            'password': 'banitsa1'
        }
    def test__form_is_not_valid__expect_success(self):
        form = CustomLoginForm(data=self.data)
        self.assertFalse(form.is_valid())