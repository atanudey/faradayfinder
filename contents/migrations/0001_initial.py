# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institute'
        db.create_table('contents_institute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Institute'])

        # Adding model 'Department'
        db.create_table('contents_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['contents.Institute'], blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Department'])

        # Adding model 'Lab'
        db.create_table('contents_lab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['custom_user.CustomUser'], blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['contents.Department'], blank=True)),
            ('primary_url', self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('meta_keyword', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['custom_user.Country'], blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=6, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(null=True, max_length=200, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(null=True, max_length=200, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(null=True, max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, max_length=75, blank=True)),
            ('video', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(null=True, max_length=75, blank=True)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Lab'])


    def backwards(self, orm):
        # Deleting model 'Institute'
        db.delete_table('contents_institute')

        # Deleting model 'Department'
        db.delete_table('contents_department')

        # Deleting model 'Lab'
        db.delete_table('contents_lab')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contents.Institute']", 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
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
            'url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['custom_user.Country']", 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['contents.Department']", 'blank': 'True'}),
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
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['custom_user.CustomUser']", 'blank': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '6', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType'},
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
            'address': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'aim': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']", 'default': "'United States'"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'verify_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': 'None', 'max_length': '32', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['contents']