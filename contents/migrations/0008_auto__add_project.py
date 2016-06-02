# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('contents_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(null=True, default=None, max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['custom_user.CustomUser'])),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['contents.Lab'])),
            ('primary_url', self.gf('django.db.models.fields.URLField')(null=True, blank=True, max_length=200)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(null=True, blank=True, max_length=200)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=255)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['custom_user.Country'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=6)),
            ('latitude', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=20)),
            ('longitude', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=20)),
            ('facebook', self.gf('django.db.models.fields.URLField')(null=True, blank=True, max_length=200)),
            ('twitter', self.gf('django.db.models.fields.URLField')(null=True, blank=True, max_length=200)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(null=True, blank=True, max_length=200)),
            ('skype', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, blank=True, max_length=75)),
            ('video', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(null=True, blank=True, max_length=75)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('contents_project')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
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
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
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
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['custom_user.Country']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['custom_user.CustomUser']"}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '6'})
        },
        'contents.project': {
            'Meta': {'object_name': 'Project'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['custom_user.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['contents.Lab']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['custom_user.CustomUser']"}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '6'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
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
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'verify_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': 'None', 'max_length': '32', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['contents']