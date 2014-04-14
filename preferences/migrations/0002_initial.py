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
            ('adj1', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('adj2', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('adj3', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('fraternity', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('party', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('novelty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clip_on', self.gf('django.db.models.fields.BooleanField')(default=True)),
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
            'clip_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fraternity': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hobby1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'hobby3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'novelty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'party': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'underwear_size': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'underwear_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['preferences']