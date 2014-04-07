from django.forms import ModelForm
from attr.models import Vertical, ProductType

class VerticalForm(ModelForm):
	class Meta:
		model = Vertical
		fields = '__all__'

class TypeForm(ModelForm):
	class Meta:
		model = ProductType
		fields = '__all__'
