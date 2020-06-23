from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # Elementi che verrano visualizzati nel form, anche se ne esistono altri, solo i seguenti verrano visualizzati
        fields = ['name', 'done']