# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonsFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age_bracket', models.SmallIntegerField(blank=True, choices=[('CHILD', 0), ('TEENAGER', 10), ('TWENTIES', 20), ('THIRTIES', 30), ('FORTIES', 40), ('FIFTIES', 50), ('SIXTIES', 60), ('SEVENTIES', 70)], null=True)),
            ],
        ),
    ]
