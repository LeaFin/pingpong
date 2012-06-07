from django.conf.urls import patterns, include, url
from scores.models import Match, Mitarbeiter
from scores.views import DateMatchListView, NameMatchListView
from django.views.generic import DetailView, ListView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^$', 'scores.views.index', name='index'),
    url(r'^name/(?P<mitarbeiter_vorname>\w+)/$', NameMatchListView.as_view()),
	url(r'^date/(?P<match_datum>[0-9\-]+)/$', DateMatchListView.as_view()),
	url(r'^detail/(?P<pk>\d+)/$', DetailView.as_view(
	model = Match,
	template_name='scores/detail.html')),
	url(r'^new_entry/$', 'scores.views.new_entry'),
	url(r'^new_entry_form/$', 'scores.views.new_entry_form', name = 'new_entry_form'),
	)
