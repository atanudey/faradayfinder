# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CustomUser.dob'
        db.add_column('custom_user_customuser', 'dob',
                      self.gf('django.db.models.fields.DateField')(blank=True, default=None, null=True),
                      keep_default=False)

        # Adding field 'CustomUser.address'
        db.add_column('custom_user_customuser', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True),
                      keep_default=False)

        # Adding field 'CustomUser.city'
        db.add_column('custom_user_customuser', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True),
                      keep_default=False)

        # Adding field 'CustomUser.state'
        db.add_column('custom_user_customuser', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True),
                      keep_default=False)

        # Adding field 'CustomUser.country'
        db.add_column('custom_user_customuser', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], default='United States'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CustomUser.dob'
        db.delete_column('custom_user_customuser', 'dob')

        # Deleting field 'CustomUser.address'
        db.delete_column('custom_user_customuser', 'address')

        # Deleting field 'CustomUser.city'
        db.delete_column('custom_user_customuser', 'city')

        # Deleting field 'CustomUser.state'
        db.delete_column('custom_user_customuser', 'state')

        # Deleting field 'CustomUser.country'
        db.delete_column('custom_user_customuser', 'country_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'custom_user.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'})
        },
        'custom_user.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']", 'default': '1'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'verify_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True', 'default': 'None', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'default': '0'})
        }
    }

    complete_apps = ['custom_user']