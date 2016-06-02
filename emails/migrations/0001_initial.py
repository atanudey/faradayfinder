# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table('emails_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True, null=True)),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('emails', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('emails_email')


    models = {
        'emails.email': {
            'Meta': {'object_name': 'Email'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'to': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['emails']