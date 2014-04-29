# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'users_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addr1', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('addr2', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True)),
            ('access_code', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('box_to_ship', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='box_to_ship', null=True, to=orm['boxes.Box'])),
            ('current_box', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='current_box ', null=True, to=orm['boxes.Box'])),
            ('preferences', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['preferences.Preferences'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['Profile'])

        # Adding M2M table for field boxes on 'Profile'
        m2m_table_name = db.shorten_name(u'users_profile_boxes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm[u'users.profile'], null=False)),
            ('box', models.ForeignKey(orm[u'boxes.box'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'box_id'])

        # Adding model 'User'
        db.create_table(u'users_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('profile', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='profile', unique=True, null=True, to=orm['users.Profile'])),
        ))
        db.send_create_signal(u'users', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'users_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'users_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'users_profile')

        # Removing M2M table for field boxes on 'Profile'
        db.delete_table(db.shorten_name(u'users_profile_boxes'))

        # Deleting model 'User'
        db.delete_table(u'users_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'users_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'users_user_user_permissions'))


    models = {
        u'attr.attr': {
            'Meta': {'object_name': 'Attr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'val': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'attr.vertical': {
            'Meta': {'object_name': 'Vertical'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'boxes.box': {
            'Meta': {'object_name': 'Box'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_delivered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['boxes.BoxFeedback']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Product']", 'symmetrical': 'False'})
        },
        u'boxes.boxfeedback': {
            'Meta': {'object_name': 'BoxFeedback'},
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'box_feedback_user'", 'symmetrical': 'False', 'to': u"orm['users.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'attrs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attr.ProductAttr']", 'symmetrical': 'False', 'blank': 'True'}),
            'duration_in_weeks': ('django.db.models.fields.IntegerField', [], {}),
            'feedback': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['products.ProductFeedback']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'items_in_box': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'items_per_purchase': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'price_per_box': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'productType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['attr.ProductType']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vertical': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['attr.Vertical']"})
        },
        u'products.productfeedback': {
            'Meta': {'object_name': 'ProductFeedback'},
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'prod_feedback_user'", 'symmetrical': 'False', 'to': u"orm['users.User']"})
        },
        u'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'access_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'addr1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'addr2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'box_to_ship': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'box_to_ship'", 'null': 'True', 'to': u"orm['boxes.Box']"}),
            'boxes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'boxes'", 'default': 'None', 'to': u"orm['boxes.Box']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'current_box': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_box '", 'null': 'True', 'to': u"orm['boxes.Box']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'preferences': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['preferences.Preferences']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['users.Profile']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['users']