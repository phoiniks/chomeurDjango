from django.contrib import admin
from .models import Angebot

# Register your models here.

class AngebotInline(admin.StackedInline):
    model = Angebot

    
class AngebotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Bezeichnung', {'fields': ['bezeichnung']}),
        ('Firma', {'fields': ['firma']}),
        ('Anzeige', {'fields': ['anzeige']}),
        ('Vorlage', {'fields': ['vorlage']}),
        ('Veröffentlichungsdatum', {'fields': ['pub_date']}),
        ('Ansprechpartner', {'fields': ['ansprechpartner']}),
        ('Anrede', {'fields': ['anrede']}),
        ('Straße', {'fields': ['strasse']}),
        ('Hausnummer', {'fields': ['hausnummer']}),
        ('Postleitzahl', {'fields': ['plz']}),
        ('Ort', {'fields': ['ort']}),
        ('Telefon (Festnetz)', {'fields': ['telefon']}),
        ('Mobiltelefon', {'fields': ['mobiltelefon']}),
        ('E-Mail', {'fields': ['email']}),
        ('Quelle', {'fields': ['quelle']}),
        ('Webseite', {'fields': ['website']}),
        ('Ergebnis', {'fields': ['ergebnis']}),
    ]

admin.site.register(Angebot, AngebotAdmin)

