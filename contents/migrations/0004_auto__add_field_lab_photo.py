# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Lab.photo'
        db.add_column('contents_lab', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Lab.photo'
        db.delete_column('contents_lab', 'photo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contents.department': {
            'Meta': {'object_name': 'Department'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'})
        },
        'contents.institute': {
            'Meta': {'object_name': 'Institute'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['custom_user.Country']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']"}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '6'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
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
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'aim': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': "'United States'", 'to': "orm['custom_user.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
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
            'linkedin': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': 'None', 'max_length': '32', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['contents']