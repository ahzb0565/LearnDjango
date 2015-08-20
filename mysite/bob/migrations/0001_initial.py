# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(max_length=200)),
                ('build_img', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_name', models.CharField(max_length=300)),
                ('result', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=300)),
                ('plan', models.ForeignKey(to='bob.ExecutionPlan')),
            ],
        ),
    ]
