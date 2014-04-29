# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Preferences'
        db.create_table(u'preferences_preferences', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('underwear_type', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('underwear_size', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('hobby1', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('hobby2', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('hobby3', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('alcohol', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('twitter_id', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('facebook_url', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('adj1', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('adj2', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('adj3', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('hair', self.gf('django.db.models.fields.BooleanField')()),
            ('sports', self.gf('django.db.models.fields.BooleanField')()),
            ('fraternity', self.gf('django.db.models.fields.BooleanField')()),
            ('party', self.gf('django.db.models.fields.BooleanField')()),
            ('novelty', self.gf('django.db.models.fields.BooleanField')()),
            ('clip_on', self.gf('django.db.models.fields.BooleanField')()),
            ('gf', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'preferences', ['Preferences'])


    def backwards(self, orm):
        # Deleting model 'Preferences'
        db.delete_table(u'preferences_preferences')


    models = {
        u'preferences.preferences': {
            'Meta': {'object_name': 'Preferences'},
            'adj1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'adj2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'adj3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'alcohol': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'clip_on': ('django.db.models.fields.BooleanField', [], {}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'fraternity': ('django.db.models.fields.BooleanField', [], {}),
            'gf': ('django.db.models.fields.BooleanField', [], {}),
            'hair': ('django.db.models.fields.BooleanField', [], {}),
            'hobby1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'novelty': ('django.db.models.fields.BooleanField', [], {}),
            'party': ('django.db.models.fields.BooleanField', [], {}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'sports': ('django.db.models.fields.BooleanField', [], {}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'underwear_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'underwear_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['preferences']