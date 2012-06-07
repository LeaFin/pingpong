from django.db import models
from django.forms import ModelForm

class Mitarbeiter(models.Model):
    vorname = models.CharField(max_length=20)
    nachname = models.CharField(max_length=20)
    geburtstag = models.DateField()
    
    def __unicode__(self):
        return self.vorname

        
    class Meta:
        verbose_name = 'Mitarbeiter'
        verbose_name_plural = 'Mitarbeiter'
    

class Match(models.Model):
    spieler_a = models.ForeignKey(Mitarbeiter, related_name='a')
    spieler_b = models.ForeignKey(Mitarbeiter, related_name='b')
    punkte_a = models.IntegerField()
    punkte_b = models.IntegerField()
    datum = models.DateField()
            
    def resultat(self):
        return '%s - %d : %d - %s' %(self.spieler_a, self.punkte_a, self.punkte_b, self.spieler_b)
    
    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'


class MatchForm(ModelForm):
    class Meta:
        model = Match
