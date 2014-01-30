from django.db import models
from box.settings import prodFeedback
from attr.models import ProductAttr

class Product(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	image_url = models.CharField(max_length=200, null=True)

	duration_in_weeks = models.IntegerField()	
	category = models.CharField(max_length=50)

	attrs = models.ManyToManyField(ProductAttr)

	feedback = models.CharField(max_length=30, choices=prodFeedback, null=True)

	item_count = models.IntegerField(default=0)
	items_per_box = models.IntegerField(default=0)
	items_per_purchase = models.IntegerField(default=1)

        def __unicode__(self):
        	return self.name

