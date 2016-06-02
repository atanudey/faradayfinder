# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table('logs_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('log_type', self.gf('django.db.models.fields.CharField')(default='debug', max_length=20)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('logs', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table('logs_log')


    models = {
        'logs.log': {
            'Meta': {'object_name': 'Log'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_type': ('django.db.models.fields.CharField', [], {'default': "'debug'", 'max_length': '20'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['logs']