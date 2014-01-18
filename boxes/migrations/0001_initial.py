# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Box'
        db.create_table(u'boxes_box', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'boxes', ['Box'])

        # Adding M2M table for field products on 'Box'
        m2m_table_name = db.shorten_name(u'boxes_box_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('box', models.ForeignKey(orm[u'boxes.box'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['box_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Box'
        db.delete_table(u'boxes_box')

        # Removing M2M table for field products on 'Box'
        db.delete_table(db.shorten_name(u'boxes_box_products'))


    models = {
        u'boxes.box': {
            'Meta': {'object_name': 'Box'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Product']", 'symmetrical': 'False'})
        },
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

    complete_apps = ['boxes']