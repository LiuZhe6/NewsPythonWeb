# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attitude', models.IntegerField()),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'browse',
            },
        ),
        migrations.CreateModel(
            name='NewModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'newsmodel',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=4)),
                ('signature', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=4)),
                ('signature', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'reader',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=30)),
                ('news', models.ForeignKey(to='newsSite.NewModel')),
            ],
            options={
                'db_table': 'source',
            },
        ),
        migrations.CreateModel(
            name='PubHeader',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='newsSite.Publisher')),
                ('url', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'pubheader',
            },
        ),
        migrations.CreateModel(
            name='ReaderHeader',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='newsSite.Reader')),
                ('url', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'readerHeader',
            },
        ),
        migrations.AddField(
            model_name='newmodel',
            name='publisher',
            field=models.ForeignKey(to='newsSite.Publisher'),
        ),
        migrations.AddField(
            model_name='browse',
            name='news',
            field=models.ForeignKey(to='newsSite.NewModel'),
        ),
        migrations.AddField(
            model_name='browse',
            name='reader',
            field=models.ForeignKey(to='newsSite.Reader'),
        ),
    ]
