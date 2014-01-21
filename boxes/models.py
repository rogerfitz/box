from django.db import models
from products.models import Product
from box.settings import feedback
from attr.models import BoxAttr

class Box(models.Model): #move to seperate app
	products = models.ManyToManyField(Product)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	feedback = models.CharField(max_length=20, choices=feedback)
	date_added = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)
	

	def __unicode__(self):
		s=''
		for product in self.products.all() :
			s+=product.name+', '
        	return s

	def getPreview(self):
		s=[]
		for product in self.products.all() :
			s.append((product.image_url, product.url))
        	return s
