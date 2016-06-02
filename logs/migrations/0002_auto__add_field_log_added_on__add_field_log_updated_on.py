# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Log.added_on'
        db.add_column('logs_log', 'added_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Log.updated_on'
        db.add_column('logs_log', 'updated_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2015, 9, 13, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Log.added_on'
        db.delete_column('logs_log', 'added_on')

        # Deleting field 'Log.updated_on'
        db.delete_column('logs_log', 'updated_on')


    models = {
        'logs.log': {
            'Meta': {'object_name': 'Log'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'debug'"}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['logs']