from django.forms import ModelForm
from django.forms.widgets import TextInput, CheckboxSelectMultiple, NumberInput
from promocodes.models import Promocode

class PromocodeCreation(ModelForm):

    class Meta:
        model = Promocode
        exclude = ['connection']
        widgets = {'listing': CheckboxSelectMultiple(attrs={"class": "kur kur kur"}),
            'percentage_off': NumberInput(attrs={"placeholder": "Проценти отстъпка", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            'code':TextInput(attrs={"placeholder": "Код", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            
        }
