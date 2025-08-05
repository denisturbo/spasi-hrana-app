from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, EmailField, ChoiceField, ImageField
from django.forms.widgets import TelInput, PasswordInput, RadioSelect, TextInput, EmailInput, FileInput
from customauth.choices import UserTypeChoices, BusinessTypeChoices
from customauth.models import BusinessUser, BaseSpasiHranaUser, CustomerUser
from django.contrib.auth.models import Group
from django.db import transaction

class CustomLoginForm(AuthenticationForm):
    username = EmailField(
        label="Потребителско име",
        widget=EmailInput(attrs={"autocomplete": "email", "placeholder": "Твоят email", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True})
    )

    
    password = CharField(
        label="Парола",
        strip=False,
        widget=PasswordInput(attrs={"placeholder": "••••••••",  "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "required": "" ,"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": (
            "Грешни данни! Моля въведете правилен %(username)s и/или парола. Имайте предвид, че "
            "и двете полета са case-sensitive."
        ),
        "inactive": ("Този акаунт изисква администраторско удобрение."),
    }


class CustomBaseSignupForm(UserCreationForm):
    password1 = CharField(
        label="Парола",
        widget=PasswordInput(attrs={
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            "autocomplete": "new-password"
        })
    )
    password2 = CharField(
        label="Повтори паролата",
        widget=PasswordInput(attrs={
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            "autocomplete": "new-password"
        })
    )

    def clean_phone_number(self):
        number = self.cleaned_data.get('phone_number')
        if number:
            cleaned = number.replace(' ', '')
            return cleaned
        return number



class CustomerSignupForm(CustomBaseSignupForm):
    first_name = CharField(
                label="Първо име",
                max_length=50, widget=TextInput(attrs={"placeholder": "Иван", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True})
                                    )
    last_name = CharField(
                label="Фамилно име",
                max_length=50, widget=TextInput(attrs={"placeholder": "Петров", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"})
                                    )


    class Meta:
        model = BaseSpasiHranaUser
        fields = ['username', 'email', 'phone_number']
        widgets = {'username':TextInput(attrs={"placeholder": "Потребителско име", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True}),
                   'email': EmailInput(attrs={"autocomplete": "email", "placeholder": "Вашият email", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"}),
                'phone_number': TelInput(attrs={"placeholder": "Тел. номер", "class": 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'})

}
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        if commit:
            user.save()
            CustomerUser.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                                      )
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
        return user


class BusinessSignupForm(CustomBaseSignupForm):
    business_name = CharField(
                label="Име на бизнес",
max_length=50, widget=TextInput(attrs={"placeholder": "Баничарницата", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True})
    )
    location = CharField(
                label="Адрес",
max_length=50, widget=TextInput(attrs={"placeholder": "ул. Лилия 1", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True})
    )
    business_type = ChoiceField(choices=BusinessTypeChoices.choices ,required=True,
                                widget=RadioSelect(attrs={"class": "w-4 h-4 text-orange-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-orange-500"}))
    profile_picture = ImageField(label="Профилна Снимка", required=True, widget=FileInput(attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"}))
    class Meta:
        model = BaseSpasiHranaUser
        fields = ['username', 'email', 'phone_number']
        widgets = {'username':TextInput(attrs={"placeholder": "Потребителско име", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True}),
                'email': EmailInput(attrs={"autocomplete": "email", "placeholder": "Твоят email", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5", "autofocus": True}),
                'phone_number': TelInput(attrs={"placeholder": "Тел. номер", "class": 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'})

}
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = UserTypeChoices.BUSINESS
        user.is_active = True # False - requires manual activation, safety reasons -- Може да бъде пуснато на True за тестове..
        if commit:
            user.save()
            BusinessUser.objects.create(
                user=user,
                business_name=self.cleaned_data['business_name'],
                location=self.cleaned_data['location'],
                business_type=self.cleaned_data['business_type'],
                profile_picture=self.cleaned_data['profile_picture'],
            )
            group = Group.objects.get(name='Business')
            user.groups.add(group)
        return user
    


