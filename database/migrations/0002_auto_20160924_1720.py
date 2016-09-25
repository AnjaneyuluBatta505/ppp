# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtopic',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='company',
            name='ceo',
        ),
        migrations.RemoveField(
            model_name='company',
            name='founded',
        ),
        migrations.RemoveField(
            model_name='company',
            name='founders',
        ),
        migrations.RemoveField(
            model_name='company',
            name='headquarters',
        ),
        migrations.AlterField(
            model_name='answer',
            name='explination',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='choice',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='history',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='why_join',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='company',
            field=models.ManyToManyField(blank=True, related_name='questions', to='database.Company'),
        ),
        migrations.AlterField(
            model_name='question',
            name='data',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.ManyToManyField(blank=True, to='database.Year'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[(b'L1', b'LEVEL1'), (b'L2', b'LEVEL2'), (b'L3', b'LEVEL3')], default=b'L1', max_length=10),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]