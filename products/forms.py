from django import forms
from .models import Product,Purchase
class purchaseForm(forms.ModelForm):
    product=forms.ModelChoiceField(queryset=Product.objects.all())
    class Meta:
        model=Purchase
        fields=['product','price','quantity']

