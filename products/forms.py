from django.forms import ModelForm
from products.models import Product
from django import forms

class ProductForm(ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Product
		exclude = ['price_per_box', 'feedback', 'item_count']

class FullProductForm(ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Product
		fields = '__all__'