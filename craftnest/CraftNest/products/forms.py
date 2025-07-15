from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'stock', 'category', 'location')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500'}),
            'category': forms.Select(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500'}),
            'location': forms.TextInput(attrs={'class': 'w-full mt-1 border px-3 py-2 rounded shadow-sm focus:ring-teal-500 focus:border-teal-500'}),
        }