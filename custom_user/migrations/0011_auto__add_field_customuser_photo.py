# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CustomUser.photo'
        db.add_column('custom_user_customuser', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CustomUser.photo'
        db.delete_column('custom_user_customuser', 'photo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType'},
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']", 'default': "'United States'"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'default': 'None', 'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': 'None', 'max_length': '32'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['custom_user']