from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	why_buy = models.TextField(max_length=1000)
	category = models.CharField(max_length=30) #add choices
	image_url = models.CharField(max_length=200)

        def __unicode__(self):
        	return self.name

