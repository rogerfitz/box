from django.contrib.auth.forms import UserCreationForm
from users.models import User, Profile
from django.forms import ModelForm
from captcha.fields import CaptchaField
from django.forms import extras
from django import forms
import datetime

class UserForm(UserCreationForm):
	captcha = CaptchaField()
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
		exclude = ['paid', 'boxes', 'box_to_ship', 'current_box']
	def __init__(self, *args, **kwargs):
		super(FullProfileForm, self).__init__(*args, **kwargs)
		self.fields['date_of_birth'].widget = extras.SelectDateWidget(years=reversed(range(datetime.date.today().year-110, datetime.date.today().year-5)))
