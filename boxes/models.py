from django.db import models
from products.models import Product
from box.settings import feedback

class Box(models.Model): #move to seperate app
	products = models.ManyToManyField(Product)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	feedback = models.CharField(max_length=20, choices=feedback)

	def __unicode__(self):
		s=''
		for product in self.products.all() :
			s+=product.name+', '
        	return s

	def getImages(self):
		s=''
		for product in self.products.all() :
			s+=product.image_url+','
		s = s.split(',')
        	return s
