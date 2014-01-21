from django.contrib.auth.forms import UserCreationForm
from users.models import User, Profile
from django.forms import ModelForm
from captcha.fields import CaptchaField

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
