from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, EmailField, ChoiceField, ModelForm
from django.forms.widgets import TelInput, PasswordInput, RadioSelect, TextInput, EmailInput
from business.models import Listing


class ListingCreation(ModelForm):

    class Meta:
        model = Listing
        fields = '__all__'
        