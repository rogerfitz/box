from django.db import models
from products.models import Product
from box.settings import boxFeedback
from attr.models import BoxAttr
from django.db.models.query import QuerySet

class Box(models.Model): #move to seperate app
	products = models.ManyToManyField(Product)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	feedback = models.CharField(max_length=20, choices=boxFeedback)#if felt cheap boost next package
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

	def distinct(self, newProducts):
		boxes= Box.objects.all()
		newNames = []
		for p in newProducts:
			newNames.append(p.name)
				
		for box in boxes:
			names = []
			products = box.products.all()
			for p in products:
				names.append(p.name)
			
			print names
			print newNames
			if len(names) == len(newNames) and len(set(names) & set(newNames)) == len(names):
				print 'false'
				return False

		return True


