from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name','slug', 'price', 'photo']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),   

        }
        

class SupplierForm(forms.ModelForm):
    class Meta:
        model = supplierinfo
        fields = '__all__'
        widgets = {
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }