# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CustomUser.is_phone_public'
        db.add_column('custom_user_customuser', 'is_phone_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.phone'
        db.add_column('custom_user_customuser', 'phone',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=15),
                      keep_default=False)

        # Adding field 'CustomUser.is_facebook_public'
        db.add_column('custom_user_customuser', 'is_facebook_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.facebook'
        db.add_column('custom_user_customuser', 'facebook',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=200),
                      keep_default=False)

        # Adding field 'CustomUser.is_linkedin_public'
        db.add_column('custom_user_customuser', 'is_linkedin_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.linkedin'
        db.add_column('custom_user_customuser', 'linkedin',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=200),
                      keep_default=False)

        # Adding field 'CustomUser.is_skype_public'
        db.add_column('custom_user_customuser', 'is_skype_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.skype'
        db.add_column('custom_user_customuser', 'skype',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50),
                      keep_default=False)

        # Adding field 'CustomUser.is_twitter_public'
        db.add_column('custom_user_customuser', 'is_twitter_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.twitter'
        db.add_column('custom_user_customuser', 'twitter',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=200),
                      keep_default=False)

        # Adding field 'CustomUser.is_aim_public'
        db.add_column('custom_user_customuser', 'is_aim_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CustomUser.aim'
        db.add_column('custom_user_customuser', 'aim',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CustomUser.is_phone_public'
        db.delete_column('custom_user_customuser', 'is_phone_public')

        # Deleting field 'CustomUser.phone'
        db.delete_column('custom_user_customuser', 'phone')

        # Deleting field 'CustomUser.is_facebook_public'
        db.delete_column('custom_user_customuser', 'is_facebook_public')

        # Deleting field 'CustomUser.facebook'
        db.delete_column('custom_user_customuser', 'facebook')

        # Deleting field 'CustomUser.is_linkedin_public'
        db.delete_column('custom_user_customuser', 'is_linkedin_public')

        # Deleting field 'CustomUser.linkedin'
        db.delete_column('custom_user_customuser', 'linkedin')

        # Deleting field 'CustomUser.is_skype_public'
        db.delete_column('custom_user_customuser', 'is_skype_public')

        # Deleting field 'CustomUser.skype'
        db.delete_column('custom_user_customuser', 'skype')

        # Deleting field 'CustomUser.is_twitter_public'
        db.delete_column('custom_user_customuser', 'is_twitter_public')

        # Deleting field 'CustomUser.twitter'
        db.delete_column('custom_user_customuser', 'twitter')

        # Deleting field 'CustomUser.is_aim_public'
        db.delete_column('custom_user_customuser', 'is_aim_public')

        # Deleting field 'CustomUser.aim'
        db.delete_column('custom_user_customuser', 'aim')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'aim': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']", 'default': "'United States'"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True', 'default': 'None'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
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
            'linkedin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '15'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': 'None', 'max_length': '32'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['custom_user']