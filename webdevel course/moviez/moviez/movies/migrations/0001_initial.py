# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movies_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('directed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Director'])),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movies', ['Movie'])

        # Adding M2M table for field starring on 'Movie'
        m2m_table_name = db.shorten_name(u'movies_movie_starring')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movies.movie'], null=False)),
            ('actor', models.ForeignKey(orm[u'movies.actor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'actor_id'])

        # Adding model 'Director'
        db.create_table(u'movies_director', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movies', ['Director'])

        # Adding model 'Actor'
        db.create_table(u'movies_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movies', ['Actor'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movies_movie')

        # Removing M2M table for field starring on 'Movie'
        db.delete_table(db.shorten_name(u'movies_movie_starring'))

        # Deleting model 'Director'
        db.delete_table(u'movies_director')

        # Deleting model 'Actor'
        db.delete_table(u'movies_actor')


    models = {
        u'movies.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'movies.director': {
            'Meta': {'object_name': 'Director'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'directed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Director']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'starring': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movies.Actor']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['movies']