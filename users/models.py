from django.db import models
from boxes.models import Box
from preferences.models import Preferences
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
import datetime

class Profile(models.Model):
	addr1 = models.CharField(max_length=50, blank=True, default="")
	addr2 = models.CharField(max_length=50, blank=True, default="")
	city = models.CharField(max_length=40, blank=True, default="")
	state = models.CharField(max_length=30, blank=True, default="")
	zipcode = models.CharField(max_length=15, blank=True, default="")
	access_code = models.CharField(max_length=60, blank=True, default="")
	
	date_of_birth = models.DateField(blank=True, null=True, help_text='Date of Birth')
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	paid = models.BooleanField(default=False, blank=True)

	boxes = models.ManyToManyField(Box, related_name='boxes', blank=True, null=True, default=None)
	box_to_ship = models.ForeignKey(Box, related_name='box_to_ship', blank=True, null=True)
	current_box = models.ForeignKey(Box, related_name='current_box ', blank=True, null=True)
	preferences = models.OneToOneField(Preferences, blank=True, null=True)

	def __unicode__(self):
        	return self.first_name+' '+self.last_name

	def ship(self):
		if self.paid is True:
			self.paid = False
			if self.current_box:
				self.boxes.add(self.current_box)
			self.current_box = self.box_to_ship
			self.box_to_ship = None
			self.date_delivered = datetime.datetime.now()
			self.save()
			send_mail('Nice Package Delivery Confirmation', 'Hi '+str(self)+",\n\nYour package has been delivered. If you didn't here us come in, sometimes we like to mix things up and deliver our nice package through the backdoor. We sincerely hope you enjoy it. To help us make your next box even better, please review the items we sent you by signing in at www.thenicepackage.com.\nThanks and have a great day!\nThe Nice Package Team\n\nIf coming through the backdoor just ain't cool with you or you have some questions, feel free to email Matteo matteo@thenicepackage.com", 'matteo@thenicepackage.com', [str(self.profile.username)], fail_silently=True)
			return self
		else:
			return self.first_name+' '+self.last_name+' needs to pay!'
	
	def pay(self):
		self.paid = True
		self.save()
		return self

	def deleteBoxToShip(self):
		self.box_to_ship = None
		self.save()
		return self

class User(AbstractUser):
	profile = models.OneToOneField(Profile, related_name='profile', unique=True, blank=True, null=True)
