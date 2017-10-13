# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4
from django.db import models
from solo.models import SingletonModel

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def upload_path_handler(instance, filename):
    return "regulamin/{hex}/{filename}".format(hex=uuid4().hex, filename=filename)


class Configuration(SingletonModel):
    rule_file = models.FileField("Plik z regulaminem", null=True, blank=True, upload_to=upload_path_handler)
    condition_file = models.FileField("Plik zformularzem zgody na wykorzystanie zdjęć", null=True, blank=True, upload_to=upload_path_handler)

    def __unicode__(self):
        return u"Konfiguracja"

    class Meta:
        verbose_name = "Konfiguracja"
