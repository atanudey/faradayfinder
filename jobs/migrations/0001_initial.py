# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table('jobs_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['custom_user.CustomUser'], blank=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'])),
            ('open_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('temporary', self.gf('django.db.models.fields.BooleanField')()),
            ('hours_per_week', self.gf('django.db.models.fields.IntegerField')()),
            ('work_schedule_summary', self.gf('django.db.models.fields.TextField')()),
            ('work_study_job', self.gf('django.db.models.fields.BooleanField')()),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Department'])),
            ('pay_rate_range_min', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
            ('pay_rate_range_max', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
            ('close_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('job_summary', self.gf('django.db.models.fields.TextField')()),
            ('responsibilities', self.gf('django.db.models.fields.TextField')()),
            ('minimum_qualification', self.gf('django.db.models.fields.TextField')()),
            ('preferences', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('additional_information', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_paid', self.gf('django.db.models.fields.BooleanField')()),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('jobs', ['Job'])

        # Adding model 'PaymentInfo'
        db.create_table('jobs_paymentinfo', (
            ('cm', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('tx', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cc', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amt', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('st', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('jobs', ['PaymentInfo'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table('jobs_job')

        # Deleting model 'PaymentInfo'
        db.delete_table('jobs_paymentinfo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'contents.institute': {
            'Meta': {'object_name': 'Institute'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['custom_user.CustomUser']", 'blank': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'ordering': "('name',)"},
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'aim': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': "'United States'", 'to': "orm['custom_user.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'default': 'None', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'default': 'None', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'default': 'None', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'default': '0'})
        },
        'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'additional_information': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'close_date': ('django.db.models.fields.DateTimeField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'hours_per_week': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_paid': ('django.db.models.fields.BooleanField', [], {}),
            'job_summary': ('django.db.models.fields.TextField', [], {}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'minimum_qualification': ('django.db.models.fields.TextField', [], {}),
            'open_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pay_rate_range_max': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'pay_rate_range_min': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'preferences': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'responsibilities': ('django.db.models.fields.TextField', [], {}),
            'temporary': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['custom_user.CustomUser']", 'blank': 'True'}),
            'work_schedule_summary': ('django.db.models.fields.TextField', [], {}),
            'work_study_job': ('django.db.models.fields.BooleanField', [], {})
        },
        'jobs.paymentinfo': {
            'Meta': {'object_name': 'PaymentInfo'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'amt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'st': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tx': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['jobs']