from django.contrib.auth.forms import UserCreationForm
from users.models import User, Profile
from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.forms import extras
from django import forms
import datetime

class UserForm(UserCreationForm):
	captcha = CaptchaField()
	
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Email'
		self.fields['username'].help_text = 'Max of 30 characters'
	def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
		username = self.cleaned_data["username"]
		try:
		    User._default_manager.get(username=username)
		except User.DoesNotExist:
		    return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])


	class Meta:
		model = User
		fields = ('username',  'password1', 'password2')

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name')

class FullProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['paid', 'boxes', 'box_to_ship', 'current_box', 'preferences', 'access_code']
	def __init__(self, *args, **kwargs):
		super(FullProfileForm, self).__init__(*args, **kwargs)
		self.fields['date_of_birth'].widget = extras.SelectDateWidget(years=reversed(range(datetime.date.today().year-110, datetime.date.today().year-5)))

class AccessForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('access_code',)
