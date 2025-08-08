import re
from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'Brand', 'model', 'Engine_no', 'Mileage',
                  'Color', 'description', 'engine', 'transmisson', 'image'}