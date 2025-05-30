from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, PasswordInput, EmailField, EmailInput

class CustomLoginForm(AuthenticationForm):
    username = EmailField(
        label=("Потребителско име"),
        widget=EmailInput(attrs={"autocomplete": "email", "placeholder": "Твоят email", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True})
    )

    
    password = CharField(
        label=("Парола"),
        strip=False,
        widget=PasswordInput(attrs={"placeholder": "••••••••",  "class":"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "required": "" ,"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": (
            "Грешни данни! Моля въведете правилен %(username)s и/или парола. Имайте предвид, че "
            "и двете полета са case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }

