import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

VORLAGEN_CHOICES = (
    ('C', 'C'),
    ('JA', 'Java'),
    ('PE', 'Perl'),
    ('PY', 'Python'),
    ('RE', 'Redaktion'),
    )

class Angebot(models.Model):
    bezeichnung = models.CharField(max_length=255)
    firma = models.CharField(max_length=255)
    anzeige = models.FileField(upload_to='anzeigen/%Y/%m/%d')
    vorlage = models.CharField(max_length=10, choices=VORLAGEN_CHOICES)
    pub_date = models.DateTimeField('Veröffentlichung')
    ansprechpartner = models.CharField(max_length=255, default="unbekannt")
    anrede = models.CharField(max_length=16, default="unbekannt")
    strasse = models.CharField('Straße', max_length=128, default="unbekannt")
    hausnummer = models.IntegerField()
    plz = models.CharField('PLZ', max_length=5, default="unbekannt")
    ort = models.CharField(max_length=255, default="unbekannt")
    telefon = models.CharField('Telefon (Festnetz)', max_length=32, default="unbekannt")
    mobiltelefon = models.CharField(max_length=32, default="unbekannt")
    email = models.CharField('E-Mail', max_length=128, default="unbekannt")
    quelle = models.CharField(max_length=128, default="unbekannt")
    website = models.CharField('Webseite', max_length=64, default="unbekannt")
    ergebnis = models.TextField(max_length=1024, default="steht noch aus")

    def __str__(self):
        return self.bezeichnung + " bei " + self.firma

    def vor_kurzem_veroeffentlicht(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"
