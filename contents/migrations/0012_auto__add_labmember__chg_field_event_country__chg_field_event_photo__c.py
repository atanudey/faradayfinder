# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LabMember'
        db.create_table('contents_labmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.CustomUser'])),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('contents', ['LabMember'])


        # Changing field 'Event.country'
        db.alter_column('contents_event', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], default='United States'))

        # Changing field 'Event.photo'
        db.alter_column('contents_event', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Event.state'
        db.alter_column('contents_event', 'state', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Event.lab'
        db.alter_column('contents_event', 'lab_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'], default=None))

        # Changing field 'Event.zipcode'
        db.alter_column('contents_event', 'zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'Event.address'
        db.alter_column('contents_event', 'address', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Event.city'
        db.alter_column('contents_event', 'city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Lab.country'
        db.alter_column('contents_lab', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], default='United States'))

        # Changing field 'Lab.photo'
        db.alter_column('contents_lab', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Lab.state'
        db.alter_column('contents_lab', 'state', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Lab.zipcode'
        db.alter_column('contents_lab', 'zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'Lab.address'
        db.alter_column('contents_lab', 'address', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Lab.city'
        db.alter_column('contents_lab', 'city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Project.country'
        db.alter_column('contents_project', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], default='United States'))

        # Changing field 'Project.photo'
        db.alter_column('contents_project', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Project.state'
        db.alter_column('contents_project', 'state', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Project.zipcode'
        db.alter_column('contents_project', 'zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'Project.address'
        db.alter_column('contents_project', 'address', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Project.city'
        db.alter_column('contents_project', 'city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Equipment.country'
        db.alter_column('contents_equipment', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], default='United States'))

        # Changing field 'Equipment.photo'
        db.alter_column('contents_equipment', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Equipment.state'
        db.alter_column('contents_equipment', 'state', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Equipment.lab'
        db.alter_column('contents_equipment', 'lab_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'], default=None))

        # Changing field 'Equipment.zipcode'
        db.alter_column('contents_equipment', 'zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'Equipment.address'
        db.alter_column('contents_equipment', 'address', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Equipment.city'
        db.alter_column('contents_equipment', 'city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

    def backwards(self, orm):
        # Deleting model 'LabMember'
        db.delete_table('contents_labmember')


        # Changing field 'Event.country'
        db.alter_column('contents_event', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], null=True))

        # Changing field 'Event.photo'
        db.alter_column('contents_event', 'photo', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

        # Changing field 'Event.state'
        db.alter_column('contents_event', 'state', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Event.lab'
        db.alter_column('contents_event', 'lab_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'], null=True))

        # Changing field 'Event.zipcode'
        db.alter_column('contents_event', 'zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=6))

        # Changing field 'Event.address'
        db.alter_column('contents_event', 'address', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Event.city'
        db.alter_column('contents_event', 'city', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Lab.country'
        db.alter_column('contents_lab', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], null=True))

        # Changing field 'Lab.photo'
        db.alter_column('contents_lab', 'photo', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

        # Changing field 'Lab.state'
        db.alter_column('contents_lab', 'state', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Lab.zipcode'
        db.alter_column('contents_lab', 'zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=6))

        # Changing field 'Lab.address'
        db.alter_column('contents_lab', 'address', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Lab.city'
        db.alter_column('contents_lab', 'city', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Project.country'
        db.alter_column('contents_project', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], null=True))

        # Changing field 'Project.photo'
        db.alter_column('contents_project', 'photo', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

        # Changing field 'Project.state'
        db.alter_column('contents_project', 'state', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Project.zipcode'
        db.alter_column('contents_project', 'zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=6))

        # Changing field 'Project.address'
        db.alter_column('contents_project', 'address', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Project.city'
        db.alter_column('contents_project', 'city', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Equipment.country'
        db.alter_column('contents_equipment', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_user.Country'], null=True))

        # Changing field 'Equipment.photo'
        db.alter_column('contents_equipment', 'photo', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

        # Changing field 'Equipment.state'
        db.alter_column('contents_equipment', 'state', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Equipment.lab'
        db.alter_column('contents_equipment', 'lab_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contents.Lab'], null=True))

        # Changing field 'Equipment.zipcode'
        db.alter_column('contents_equipment', 'zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=6))

        # Changing field 'Equipment.address'
        db.alter_column('contents_equipment', 'address', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

        # Changing field 'Equipment.city'
        db.alter_column('contents_equipment', 'city', self.gf('django.db.models.fields.CharField')(null=True, max_length=100))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']", 'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'})
        },
        'contents.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']", 'blank': 'True', 'null': 'True'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']", 'blank': 'True', 'null': 'True'}),
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
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'})
        },
        'contents.lab': {
            'Meta': {'object_name': 'Lab'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.Country']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Institute']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']", 'blank': 'True', 'null': 'True'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'facebook': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contents.Lab']", 'blank': 'True', 'null': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'longitude': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'meta_abstract': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'paypal_account': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'primary_twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'primary_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_user.CustomUser']", 'blank': 'True', 'null': 'True'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': "'United States'", 'to': "orm['custom_user.Country']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'tnc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'verify_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'blank': 'True', 'null': 'True', 'max_length': '32'}),
            'zipcode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '6'})
        }
    }

    complete_apps = ['contents']