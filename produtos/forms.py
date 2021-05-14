from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code', 'quantity', 'price', 'description', 'product_image']