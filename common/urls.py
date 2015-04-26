from django.conf.urls import patterns, url
from common import views

urlpatterns = patterns('',
        url(r'team/(?P<team_id>\d+)/tweet', views.team_tweet, name='team_tweet'),
        url(r'team/(?P<team_id>\d+)', views.team_show, name='team_show'),
        url(r'$', views.team_list, name='team_list'),
)
