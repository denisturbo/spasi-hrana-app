from django.forms import ModelForm
from django.forms.widgets import TextInput, Select, NumberInput
from promocodes.models import Promocode

class PromocodeCreation(ModelForm):

    class Meta:
        model = Promocode
        exclude = ['connection']
        widgets = {'listing':Select(attrs={"class": "w-4 h-4 text-orange-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-orange-500"}),
            'percentage_off': NumberInput(attrs={"placeholder": "Проценти отстъпка", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            'code':TextInput(attrs={"placeholder": "Код", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            
        }
