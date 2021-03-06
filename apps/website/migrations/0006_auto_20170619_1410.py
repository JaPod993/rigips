# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import website.models.configuration


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_configuration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='rule_file',
            field=models.FileField(blank=True, null=True, upload_to=website.models.configuration.upload_path_handler, verbose_name='Plik z regulaminem'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='category',
            field=models.CharField(choices=[('1', 'P\u0142yty gipsowo-kartonowe'), ('2', 'Rozwi\u0105zania innowacyjne i nienaruszaj\u0105ce r\xf3wnowagi \u015brodowiskowej'), ('3', 'Budynki mieszkalne'), ('4', 'Rozwi\u0105zania sektorowe'), ('5', 'Sufity')], max_length=255, verbose_name='Kategoria konkursowa'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Faks'),
        ),
    ]
