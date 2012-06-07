from scores.models import Mitarbeiter, Match
from django.contrib import admin

class MitarbeiterAdmin(admin.ModelAdmin):
	fieldsets = [('Personalien', {'fields': ['vorname', 'nachname', 'geburtstag']}),]
	list_display = ('vorname', 'nachname', 'geburtstag')


class MatchAdmin(admin.ModelAdmin):
	list_display = ('datum', 'resultat')
	list_filter = ['spieler_a__vorname', 'spieler_b__vorname']
	search_fields = ['spieler_a__vorname', 'spieler_b__vorname']
	fields = ['spieler_a', 'spieler_b', 'punkte_a', 'punkte_b', 'datum']

admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(Match, MatchAdmin)
