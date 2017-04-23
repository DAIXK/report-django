# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('order', models.CharField(max_length=50, verbose_name='\u8ba2\u5355\u53f7', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u5ba2\u6237\u59d3\u540d', blank=True)),
                ('sn', models.CharField(max_length=30)),
                ('question', models.CharField(max_length=300, verbose_name='\u95ee\u9898\u63cf\u8ff0', blank=True)),
                ('question_type', models.CharField(max_length=20, verbose_name='\u4e0d\u826f\u7c7b\u578b')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u914d\u4ef6\u6570\u636e',
                'verbose_name_plural': '\u914d\u4ef6\u6570\u636e',
            },
        ),
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name': '\u76d2\u5b50\u6570\u636e', 'verbose_name_plural': '\u76d2\u5b50\u6570\u636e'},
        ),
    ]
