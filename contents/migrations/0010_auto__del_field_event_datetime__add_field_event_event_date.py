# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.datetime'
        db.delete_column('contents_event', 'datetime')

        # Adding field 'Event.event_date'
        db.add_column('contents_event', 'event_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 10, 10, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.datetime'
        db.add_column('contents_event', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 10, 10, 0, 0)),
                      keep_default=False)

        # Deleting field 'Event.event_date'
        db.delete_column('contents_event', 'event_date')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contents.department': {
            'Meta': {'object_name': 'Department'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contents.Institute']", 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'contents.event': {
            'Meta': {'object_name': 'Event'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.Country']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contents.Lab']", 'null': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '6', 'null': 'True'})
        },
        'contents.institute': {
            'Meta': {'object_name': 'Institute'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.Country']", 'null': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '6', 'null': 'True'})
        },
        'contents.project': {
            'Meta': {'object_name': 'Project'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.Country']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contents.Lab']", 'null': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '6', 'null': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'custom_user.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '200'})
        },
        'custom_user.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'aim': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']", 'default': "'United States'"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_aim_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_facebook_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_linkedin_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_phone_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_skype_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_twitter_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '32', 'default': 'None', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'default': '0'})
        }
    }

    complete_apps = ['contents']