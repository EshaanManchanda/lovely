
from django import forms
from .models import Inventory  

class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory  # Specify the model class
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']

class UpdateInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory  # Specify the model class
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']
