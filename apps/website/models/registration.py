# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField


_UNSAVED_FILEFIELD = 'unsaved_filefield'


def upload_path_handler(instance, filename):
    return "registration/{id}/images/{filename}".format(id=instance.registration_id, filename=filename)


def upload_path_handler_scan(instance, filename):
    return "registration/{id}/scans/{filename}".format(id=instance.pk, filename=filename)


class Registration(models.Model):

    CATEGORY_CHOICES = (
        ("1", "Płyty gipsowo-kartonowe"),
        ("2", "Rozwiązania innowacyjne i nienaruszające równowagi środowiskowej"),
        ("3", "Budynki mieszkalne"),
        ("4", "Rozwiązania sektorowe"),
        ("5", "Sufity"),
    )

    created_at = models.DateTimeField("Data utworzenia", auto_now_add=True)
    company_name = models.CharField("Nazwa firmy", max_length=255)
    category = MultiSelectField("Kategoria konkursowa", max_length=255, choices=CATEGORY_CHOICES)
    name = models.CharField("Imię i nazwisko", max_length=255)
    company_address = models.TextField("Adres firmy", default="")
    phone = models.CharField("Telefon", max_length=255)
    fax = models.CharField("Faks", max_length=255, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=255)
    allow_scan = models.FileField("Skan zgody", blank=True, null=True, upload_to=upload_path_handler_scan)
    description_1 = models.TextField("Krótki opis budowy", default="")
    description_2 = models.TextField("Zastosowane rozwiązania", default="")
    description_3 = models.TextField("Zastosowane systemy Rigips",
                                     default="",
                                     help_text="Rozwiązania, które wyróżniają projekt np nietypowe pomieszczenie, "
                                               "krótki czas realizacji przy skomplikowanych rozwiązaniach, "
                                               "dźwięko-chłonność, zabezpieczenia, nietypowe rozwiązania ppoż.")

    class Meta:
        app_label = 'website'
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"

    def __unicode__(self):
        return self.name


class RegistrationFile(models.Model):

    registration = models.ForeignKey("website.Registration")
    created_at = models.DateTimeField("Data utworzenia", auto_now_add=True)
    file = models.FileField("Załacznik", upload_to=upload_path_handler)

    app_label = 'website'
    verbose_name = "Załącznik"
    verbose_name_plural = "Załączniki"


@receiver(pre_save, sender=Registration)
def skip_saving_scan(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.allow_scan)
        instance.allow_scan = None


@receiver(post_save, sender=Registration)
def save_scan(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.allow_scan = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()


@receiver(pre_save, sender=RegistrationFile)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.file)
        instance.file = None


@receiver(post_save, sender=RegistrationFile)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.file = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
