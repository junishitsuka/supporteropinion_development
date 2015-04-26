from django.conf.urls import patterns, url
from common import views

urlpatterns = patterns('',
        url(r'team/(?P<team_id>\d+)', views.team_show, name='team_show'),
        url(r'add', views.team_edit, name='team_add'),
        url(r'edit/(?P<team_id>\d+)', views.team_edit, name='team_edit'),
        url(r'delete/(?P<team_id>\d+)', views.team_delete, name='team_delete'),
        url(r'$', views.team_list, name='team_list'),
)
