from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date_added', 'image']
        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date'})
        }


class ProductId(forms.Form):
    product_id = forms.IntegerField(label='Product ID')

    def clean_product_id(self):
        product_id = self.cleaned_data['product_id']
        if not Product.objects.filter(pk=product_id).exists():
            raise ValidationError('Product with this ID does not exist.')
        return product_id