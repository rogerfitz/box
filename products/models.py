from django.db import models
from box.settings import prodFeedback
from attr.models import ProductAttr, ProductType, Vertical
from django import forms

class ProductFeedback(models.Model):
	feedback = models.CharField(max_length=20, choices=prodFeedback)
	user = models.ManyToManyField('users.User', related_name='prod_feedback_user')
	
	def __unicode__(self):
		return self.feedback

class Product(models.Model):
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=200, blank=True, null=True, default=None)
	product_line = models.CharField(max_length=200, blank=True, null=True, default=None)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	price_per_box = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	image_url = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=300)

	duration_in_weeks = models.IntegerField()

	productType = models.ForeignKey(ProductType)
	vertical = models.ForeignKey(Vertical)

	attrs = models.ManyToManyField(ProductAttr, blank=True)

	feedback = models.ManyToManyField(ProductFeedback, blank=True, null=True, default=None)

	item_count = models.IntegerField(default=0)
	items_in_box = models.IntegerField(default=1)
	items_per_purchase = models.IntegerField(default=1)

        def __unicode__(self):
        	return self.name

	def save(self, *args, **kwargs):
		self.price_per_box = self.price*self.items_in_box/self.items_per_purchase
		super(Product, self).save(*args, **kwargs)

	def getMetrics(self):
		likes = (self.feedback.filter(feedback='like')).count()
		oks = (self.feedback.filter(feedback='ok')).count()
		dislikes = (self.feedback.filter(feedback='dislike')).count()
		have = (self.feedback.filter(feedback='already have')).count()
		return [likes, oks, dislikes, have]
