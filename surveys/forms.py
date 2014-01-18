from django.forms import ModelForm
from surveys.models import ProductSurvey, BoxSurvey

class ProductSurveyForm(ModelForm):
	class Meta:
		model = ProductSurvey
		fields = '__all__' #exclude Box or Product

class BoxSurveyForm(ModelForm):
	class Meta:
		model = BoxSurvey
		fields = '__all__' #exclude Box or Product
