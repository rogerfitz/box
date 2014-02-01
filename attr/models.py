from django.db import models

class Attr(models.Model):
	key = models.CharField(max_length=30)
	val = models.CharField(max_length=50)

class ProfileAttr(Attr):
	prof_id = models.IntegerField()

class ProductAttr(Attr):
	product_id = models.IntegerField()

class BoxAttr(Attr):
	box_id = models.IntegerField()

class Vertical(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class ProductType(models.Model):
	vertical = models.ForeignKey(Vertical)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
