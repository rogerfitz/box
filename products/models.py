from django.db import models
from box.settings import prodFeedback
from attr.models import ProductAttr, ProductType, Vertical

class Product(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	price_per_box = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	image_url = models.CharField(max_length=200, null=True)

	duration_in_weeks = models.IntegerField()

	productType = models.ForeignKey(ProductType)
	vertical = models.ForeignKey(Vertical)

	attrs = models.ManyToManyField(ProductAttr, blank=True)

	feedback = models.CharField(max_length=30, choices=prodFeedback, blank=True, default=None, null=True)

	item_count = models.IntegerField(default=0)
	items_in_box = models.IntegerField(default=1)
	items_per_purchase = models.IntegerField(default=1)

        def __unicode__(self):
        	return self.name

