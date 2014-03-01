# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'go_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('player1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_player1', to=orm['auth.User'])),
            ('player2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_player2', to=orm['auth.User'])),
            ('board_size', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=19)),
        ))
        db.send_create_signal(u'go', ['Game'])

        # Adding model 'Play'
        db.create_table(u'go_play', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['go.Game'])),
            ('seq', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('player', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('loc', self.gf('django.db.models.fields.CharField')(max_length='7')),
        ))
        db.send_create_signal(u'go', ['Play'])

        # Adding unique constraint on 'Play', fields ['game', 'seq']
        db.create_unique(u'go_play', ['game_id', 'seq'])


    def backwards(self, orm):
        # Removing unique constraint on 'Play', fields ['game', 'seq']
        db.delete_unique(u'go_play', ['game_id', 'seq'])

        # Deleting model 'Game'
        db.delete_table(u'go_game')

        # Deleting model 'Play'
        db.delete_table(u'go_play')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'go.game': {
            'Meta': {'object_name': 'Game'},
            'board_size': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '19'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_player1'", 'to': u"orm['auth.User']"}),
            'player2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_player2'", 'to': u"orm['auth.User']"})
        },
        u'go.play': {
            'Meta': {'unique_together': "(('game', 'seq'),)", 'object_name': 'Play'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['go.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc': ('django.db.models.fields.CharField', [], {'max_length': "'7'"}),
            'player': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'seq': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['go']