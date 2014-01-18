from django.db import models
from products.models import Product
from boxes.models import Box
from users.models import User

ratings=((0, 0), (.5, .5), (1, 1), (1.5, 1.5), (2, 2) ,(2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))

class ProductSurvey(models.Model):
	rating = models.DecimalField(max_digits=1, decimal_places=1, choices=ratings, help_text='How much did you like this product?')
	product = models.OneToOneField(Product, blank=True, null=True)
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.product.name


class BoxSurvey(models.Model): 
	rating = models.DecimalField(max_digits=1, decimal_places=1, choices=ratings, help_text='How much did you like this product?')
	box = models.OneToOneField(Box, blank=True, null=True)
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.box
