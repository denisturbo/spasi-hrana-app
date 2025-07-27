import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class BulgarianPhoneNumberValidator:
    regex = r'^(\+)?(359|0)8[789]\d{7}$'
    message = "Моля въведете валиден български телефонен номер."
    code = 'invalid_phone_number'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not re.match(self.regex, value):
            raise ValidationError(self.message, code=self.code)