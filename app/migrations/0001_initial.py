# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('order', models.CharField(max_length=40, verbose_name='\u8ba2\u5355\u53f7')),
                ('name', models.CharField(max_length=40, verbose_name='\u59d3\u540d', blank=True)),
                ('sn', models.CharField(unique=True, max_length=20, verbose_name='SN')),
                ('mac', models.CharField(max_length=20, verbose_name='MAC', blank=True)),
                ('question', models.CharField(max_length=300, verbose_name='\u95ee\u9898\u63cf\u8ff0', blank=True)),
                ('remarks', models.CharField(max_length=20, verbose_name='\u5224\u65ad\u8868\u5f81', blank=True)),
                ('question_type', models.CharField(max_length=5, verbose_name='\u4e0d\u826f\u7c7b\u578b')),
                ('reason', models.CharField(max_length=10, verbose_name='\u6839\u672c\u539f\u56e0')),
                ('result', models.CharField(max_length=10, verbose_name='\u539f\u56e0\u5f52\u7c7b')),
                ('version', models.CharField(max_length=10, verbose_name='\u578b\u53f7')),
                ('data', models.CharField(max_length=10, verbose_name='\u6279\u6b21\u65e5\u671f')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u76d2\u5b50\u552e\u540e\u6570\u636e',
                'verbose_name_plural': '\u76d2\u5b50\u552e\u540e\u6570\u636e',
            },
        ),
    ]
