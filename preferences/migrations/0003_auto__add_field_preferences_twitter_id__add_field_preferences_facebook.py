# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Preferences.twitter_id'
        db.add_column(u'preferences_preferences', 'twitter_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Preferences.facebook_url'
        db.add_column(u'preferences_preferences', 'facebook_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Preferences.sports'
        db.add_column(u'preferences_preferences', 'sports',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Preferences.gf'
        db.add_column(u'preferences_preferences', 'gf',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Preferences.twitter_id'
        db.delete_column(u'preferences_preferences', 'twitter_id')

        # Deleting field 'Preferences.facebook_url'
        db.delete_column(u'preferences_preferences', 'facebook_url')

        # Deleting field 'Preferences.sports'
        db.delete_column(u'preferences_preferences', 'sports')

        # Deleting field 'Preferences.gf'
        db.delete_column(u'preferences_preferences', 'gf')


    models = {
        u'preferences.preferences': {
            'Meta': {'object_name': 'Preferences'},
            'adj1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'adj2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'adj3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'alcohol': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'clip_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'fraternity': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'gf': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hobby1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'novelty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'party': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'sports': ('django.db.models.fields.BooleanField', [], {}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'underwear_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'underwear_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['preferences']