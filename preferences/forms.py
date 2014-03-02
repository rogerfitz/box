from django.forms import ModelForm
from preferences.models import Preferences

class PreferencesForm(ModelForm):
	class Meta:
		model = Preferences
		fields = '__all__'

