# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('university_id', models.CharField(default=None, max_length=100)),
                ('_university_name', models.CharField(default=None, max_length=100)),
                ('_email', models.EmailField(default=None, max_length=75)),
                ('_address', models.CharField(max_length=500, default=None, null=True)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('college_name', models.CharField(default=None, max_length=100)),
                ('college_id', models.CharField(primary_key=True, default=None, max_length=100, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
