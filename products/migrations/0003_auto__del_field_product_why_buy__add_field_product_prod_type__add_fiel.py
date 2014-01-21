# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.why_buy'
        db.delete_column(u'products_product', 'why_buy')

        # Adding field 'Product.prod_type'
        db.add_column(u'products_product', 'prod_type',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=50),
                      keep_default=False)

        # Adding field 'Product.duration_in_weeks'
        db.add_column(u'products_product', 'duration_in_weeks',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Product.feedback'
        db.add_column(u'products_product', 'feedback',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'Product.send_similar'
        db.add_column(u'products_product', 'send_similar',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Product.item_count'
        db.add_column(u'products_product', 'item_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Product.image_url'
        db.alter_column(u'products_product', 'image_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'Product.why_buy'
        db.add_column(u'products_product', 'why_buy',
                      self.gf('django.db.models.fields.TextField')(default=' ', max_length=1000),
                      keep_default=False)

        # Deleting field 'Product.prod_type'
        db.delete_column(u'products_product', 'prod_type')

        # Deleting field 'Product.duration_in_weeks'
        db.delete_column(u'products_product', 'duration_in_weeks')

        # Deleting field 'Product.feedback'
        db.delete_column(u'products_product', 'feedback')

        # Deleting field 'Product.send_similar'
        db.delete_column(u'products_product', 'send_similar')

        # Deleting field 'Product.item_count'
        db.delete_column(u'products_product', 'item_count')


        # Changing field 'Product.image_url'
        db.alter_column(u'products_product', 'image_url', self.gf('django.db.models.fields.CharField')(default=' ', max_length=200))

    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'duration_in_weeks': ('django.db.models.fields.IntegerField', [], {}),
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'prod_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'send_similar': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['products']