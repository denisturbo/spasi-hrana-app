from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput, Textarea, FileInput
from business.models import Listing


class ListingCreation(ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'image', 'price']
        widgets = {'title': TextInput(attrs={"placeholder": "Заглавие", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
                   'description': Textarea(attrs={"placeholder": "Описание на продукта", "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none", "autofocus": True}),
                   'image': FileInput(attrs={"class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"}),
                   'price':NumberInput(attrs={"placeholder": "Цена", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            
        }
        