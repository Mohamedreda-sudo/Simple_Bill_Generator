from django import forms
from .models import BoughtItem

class BoughtItemForm(forms.ModelForm):
    class Meta:
        model = BoughtItem
        fields = ['name', 'price']
