# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import database.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('explination', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to=database.models.url, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=database.models.url, blank=True)),
                ('is_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('ceo', models.CharField(max_length=50, null=True, blank=True)),
                ('founded', models.DateTimeField(blank=True)),
                ('founders', models.CharField(max_length=50, null=True, blank=True)),
                ('headquarters', models.CharField(max_length=50, null=True, blank=True)),
                ('about', models.CharField(max_length=1000, null=True)),
                ('history', models.CharField(max_length=1000, null=True)),
                ('why_join', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=1000, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=database.models.url, blank=True)),
                ('level', models.CharField(max_length=10, choices=[(b'L1', b'LEVEL1'), (b'L2', b'LEVEL2'), (b'L3', b'LEVEL3')])),
                ('company', models.ManyToManyField(to='database.Company', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(related_name='sub_topics', to='database.Topic'),
        ),
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.ManyToManyField(to='database.Year'),
        ),
        migrations.AddField(
            model_name='question',
            name='reference',
            field=models.ForeignKey(blank=True, to='database.Question', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_topic',
            field=models.ForeignKey(to='database.SubTopic'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='database.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='database.Question'),
        ),
    ]
