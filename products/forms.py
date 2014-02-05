from django.forms import ModelForm
from products.models import Product

class ProductForm(ModelForm):
	class Meta:
		model = Product
		exclude = ['price_per_box', 'feedback', 'item_count']

