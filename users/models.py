from django.db import models
from boxes.models import Box
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
	addr1 = models.CharField(max_length=50, blank=True, null=True)
	addr2 = models.CharField(max_length=50, blank=True, null=True)
	city = models.CharField(max_length=40, blank=True, null=True)
	state = models.CharField(max_length=30, blank=True, null=True)
	zipcode = models.CharField(max_length=15, blank=True, null=True)
	
	date_of_birth = models.DateField(null=True)
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	paid = models.BooleanField(default=False, blank=True)

	boxes = models.ManyToManyField(Box, related_name='boxes', blank=True, null=True, default=None)
	box_to_ship = models.ForeignKey(Box, related_name='box_to_ship', blank=True, null=True)
	current_box = models.ForeignKey(Box, related_name='current_box ', blank=True, null=True)

	def __unicode__(self):
        	return self.first_name+' '+self.last_name

class User(AbstractUser):
	profile = models.OneToOneField(Profile, related_name='profile', unique=True, blank=True, null=True)

class Attribute(models.Model):
	key = models.CharField(max_length=30)
	val = models.CharField(max_length=50)
	prof_id = models.IntegerField()
