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
            ('url', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Institute'])

        # Adding model 'Department'
        db.create_table('contents_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['contents.Institute'], null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('order_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Department'])

        # Adding model 'Lab'
        db.create_table('contents_lab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['custom_user.CustomUser'], null=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Institute'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Department'])),
            ('primary_url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('latitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Lab'])

        # Adding model 'LabMember'
        db.create_table('contents_labmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.CustomUser'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('contents', ['LabMember'])

        # Adding model 'Project'
        db.create_table('contents_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['custom_user.CustomUser'], null=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['contents.Lab'], null=True)),
            ('primary_url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('latitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Project'])

        # Adding model 'Event'
        db.create_table('contents_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['custom_user.CustomUser'], null=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'])),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('primary_url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('latitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Event'])

        # Adding model 'Equipment'
        db.create_table('contents_equipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['custom_user.CustomUser'], null=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'])),
            ('primary_url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('primary_twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('meta_abstract', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('latitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=15, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('paypal_account', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('tnc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('contents', ['Equipment'])

        # Adding model 'ChatMessages'
        db.create_table('contents_chatmessages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender_email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('receiver_email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, null=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('contents', ['ChatMessages'])


    def backwards(self, orm):
        # Deleting model 'Institute'
        db.delete_table('contents_institute')

        # Deleting model 'Department'
        db.delete_table('contents_department')

        # Deleting model 'Lab'
        db.delete_table('contents_lab')

        # Deleting model 'LabMember'
        db.delete_table('contents_labmember')

        # Deleting model 'Project'
        db.delete_table('contents_project')

        # Deleting model 'Event'
        db.delete_table('contents_event')

        # Deleting model 'Equipment'
        db.delete_table('contents_equipment')

        # Deleting model 'ChatMessages'
        db.delete_table('contents_chatmessages')


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
        'contents.chatmessages': {
            'Meta': {'object_name': 'ChatMessages'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'receiver_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'sender_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'})
        },
        'contents.department': {
            'Meta': {'object_name': 'Department'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contents.Institute']", 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'contents.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contents.event': {
            'Meta': {'object_name': 'Event'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contents.institute': {
            'Meta': {'object_name': 'Institute'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contents.labmember': {
            'Meta': {'object_name': 'LabMember'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']"})
        },
        'contents.project': {
            'Meta': {'object_name': 'Project'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['contents.Lab']", 'null': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['custom_user.CustomUser']", 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)"},
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
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'aim': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': "'United States'", 'to': "orm['custom_user.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
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
            'linkedin': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100', 'default': 'None', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '32', 'default': 'None', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'default': '0'})
        }
    }

    complete_apps = ['contents']