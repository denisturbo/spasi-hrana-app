from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, PasswordInput, EmailField, EmailInput, ChoiceField, TextInput
from customauth.models import BusinessUser, BaseSpasiHranaUser, CustomerUser

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
        "inactive": ("Този акаунт изисква администраторско удобрение."),
    }

class CustomerSignupForm(UserCreationForm):
    first_name = CharField(
                label=("Първо име"),
                max_length=50, widget=TextInput(attrs={"placeholder": "Иван", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True})
                                    )
    last_name = CharField(
                label=("Фамилно име"),
                max_length=50, widget=TextInput(attrs={"placeholder": "Петров", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True})
                                    )

    password1 = CharField(
        label="Парола",
        widget=PasswordInput(attrs={
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5",
            "autocomplete": "new-password"
        })
    )
    password2 = CharField(
        label="Повтори паролата",
        widget=PasswordInput(attrs={
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5",
            "autocomplete": "new-password"
        })
    )


    class Meta:
        model = BaseSpasiHranaUser
        fields = ['username', 'email']
        widgets = {'username':TextInput(attrs={"placeholder": "Потребителско име", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
                   'email': EmailInput(attrs={"autocomplete": "email", "placeholder": "Твоят email", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),

}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        if commit:
            user.save()
            CustomerUser.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name']
            )
        return user


class BusinessSignupForm(CustomerSignupForm):
    business_name = CharField(
                label=("Име на бизнес"),
max_length=50, widget=TextInput(attrs={"placeholder": "Баничарницата", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True})
    )
    location = CharField(
                label=("Адрес"),
max_length=50, widget=TextInput(attrs={"placeholder": "ул. Лилия 1", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True})
    )
    business_type = ChoiceField(choices=BusinessUser.BUSINESS_TYPE_CHOICES)

    class Meta:
        model = BaseSpasiHranaUser
        fields = ['username', 'email']
        widgets = {'username':TextInput(attrs={"placeholder": "Потребителско име", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
                'email': EmailInput(attrs={"autocomplete": "email", "placeholder": "Твоят email", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),

}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'business'
        user.is_active = False # False - requires manual activation, safety reasons -- Може да бъде пуснато на True за тестове..
        if commit:
            user.save()
            BusinessUser.objects.create(
                user=user,
                business_name=self.cleaned_data['business_name'],
                location=self.cleaned_data['location'],
                business_type=self.cleaned_data['business_type']
            )
        return user