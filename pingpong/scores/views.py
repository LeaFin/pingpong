from datetime import date, datetime

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import Context, loader
from django.views.generic import ListView

from scores.models import Match, Mitarbeiter, MatchForm


def index(request):
    latest_matches = Match.objects.order_by('-datum')
    spieler = Mitarbeiter.objects.order_by('vorname')
    
    # temp = loader.get_template('scores/index.html')
    # con = Context({
    # 'latest_matches': latest_matches,
    # 'spieler': spieler,
    # })
    # return HttpResponse(temp.render(con))
    return render(request, 'scores/index.html',{
        'latest_matches': latest_matches,
        'spieler': spieler,
        })

    
class DateMatchListView(ListView):
    context_object_name = 'match_list'
    template_name = 'scores/match_list'
    
    def get_queryset(self):
        date = self.kwargs['match_datum']
        date_c = datetime.strptime ( date, '%Y-%m-%d')
        return Match.objects.filter(datum = date_c)


class NameMatchListView(ListView):
    context_object_name = 'match_list'
    template_name = 'scores/match_list'
    
    def get_queryset(self):
        name = self.kwargs['mitarbeiter_vorname']
        return Match.objects.filter(Q(gewinner__vorname = name) | Q(verlierer__vorname = name))
        
def new_entry_form(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            spieler_a = form.cleaned_data['spieler_a']
            spieler_b = form.cleaned_data['spieler_b']
            punkte_a = form.cleaned_data['punkte_a']
            punkte_b = form.cleaned_data['punkte_b']
            # datum = form.cleand_data['datum']
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    else:
        form = MatchForm()
    
    return render(request, 'scores/resultat_form.html', {'form':form})

def new_entry(request):
    return HttpResponseRedirect(reverse('new_entry_form'))
    