from django.forms import ModelForm
from django.forms.widgets import TextInput, CheckboxSelectMultiple, NumberInput

from listings.models import Listing
from promocodes.models import Promocode

class PromocodeCreation(ModelForm):

    class Meta:
        model = Promocode
        exclude = ['connection']
        widgets = {'listing': CheckboxSelectMultiple(),
            'percentage_off': NumberInput(attrs={"placeholder": "Проценти отстъпка", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5", "autofocus": True}),
            'code':TextInput(attrs={"placeholder": "Код", "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}),
            
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['listing'].queryset = Listing.objects.filter(connection=user.businessuser)


class EditPromocode(PromocodeCreation):
    ...