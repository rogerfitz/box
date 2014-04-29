# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attr'
        db.create_table(u'attr_attr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('val', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'attr', ['Attr'])

        # Adding model 'ProfileAttr'
        db.create_table(u'attr_profileattr', (
            (u'attr_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['attr.Attr'], unique=True, primary_key=True)),
            ('prof_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'attr', ['ProfileAttr'])

        # Adding model 'ProductAttr'
        db.create_table(u'attr_productattr', (
            (u'attr_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['attr.Attr'], unique=True, primary_key=True)),
            ('product_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'attr', ['ProductAttr'])

        # Adding model 'BoxAttr'
        db.create_table(u'attr_boxattr', (
            (u'attr_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['attr.Attr'], unique=True, primary_key=True)),
            ('box_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'attr', ['BoxAttr'])

        # Adding model 'Vertical'
        db.create_table(u'attr_vertical', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'attr', ['Vertical'])

        # Adding model 'ProductType'
        db.create_table(u'attr_producttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vertical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['attr.Vertical'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'attr', ['ProductType'])


    def backwards(self, orm):
        # Deleting model 'Attr'
        db.delete_table(u'attr_attr')

        # Deleting model 'ProfileAttr'
        db.delete_table(u'attr_profileattr')

        # Deleting model 'ProductAttr'
        db.delete_table(u'attr_productattr')

        # Deleting model 'BoxAttr'
        db.delete_table(u'attr_boxattr')

        # Deleting model 'Vertical'
        db.delete_table(u'attr_vertical')

        # Deleting model 'ProductType'
        db.delete_table(u'attr_producttype')


    models = {
        u'attr.attr': {
            'Meta': {'object_name': 'Attr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'attr.boxattr': {
            'Meta': {'object_name': 'BoxAttr', '_ormbases': [u'attr.Attr']},
            u'attr_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['attr.Attr']", 'unique': 'True', 'primary_key': 'True'}),
            'box_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'attr.productattr': {
            'Meta': {'object_name': 'ProductAttr', '_ormbases': [u'attr.Attr']},
            u'attr_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['attr.Attr']", 'unique': 'True', 'primary_key': 'True'}),
            'product_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'attr.producttype': {
            'Meta': {'object_name': 'ProductType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vertical': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['attr.Vertical']"})
        },
        u'attr.profileattr': {
            'Meta': {'object_name': 'ProfileAttr', '_ormbases': [u'attr.Attr']},
            u'attr_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['attr.Attr']", 'unique': 'True', 'primary_key': 'True'}),
            'prof_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'attr.vertical': {
            'Meta': {'object_name': 'Vertical'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['attr']