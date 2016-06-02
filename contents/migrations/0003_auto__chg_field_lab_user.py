# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Lab.user'
        db.alter_column('contents_lab', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.CustomUser'], default=None))

    def backwards(self, orm):

        # Changing field 'Lab.user'
        db.alter_column('contents_lab', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['custom_user.CustomUser']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contents.department': {
            'Meta': {'object_name': 'Department'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contents.Institute']", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'contents.institute': {
            'Meta': {'object_name': 'Institute'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['custom_user.Country']", 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '15', 'blank': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']"}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '6', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
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
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'aim': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': "'United States'", 'to': "orm['custom_user.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']"}),
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
            'linkedin': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '15', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '32', 'blank': 'True', 'default': 'None'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'default': '0'})
        }
    }

    complete_apps = ['contents']