from django.db import models
from box.settings import feedback

class Product(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	image_url = models.CharField(max_length=200, null=True)

	prod_type = models.CharField(max_length=50)
	duration_in_weeks = models.IntegerField()	
	
	category = models.CharField(max_length=30) #add choices
	feedback = models.CharField(max_length=20, choices=feedback, null=True)
	send_similar = models.BooleanField(default = True)

	item_count = models.IntegerField(default=0)
	items_per_box = models.IntegerField(default=0)

        def __unicode__(self):
        	return self.name

