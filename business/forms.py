from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput
from business.models import Listing


class ListingCreation(ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'price']
        widgets = {'title': TextInput(attrs={"placeholder": "Заглавие", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
                   'description': TextInput(attrs={"placeholder": "Описание на продукта", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
                   'price':NumberInput(attrs={"placeholder": "Потребителско име", "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            
        }
        