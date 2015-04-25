from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
        url(r'^common/$', views.team_list, name='team_list'),
        url(r'^common/add', views.team_edit, name='team_edit'),
        url(r'^common/edit', views.team_edit, name='team_edit'),
        url(r'^common/delete', views.team_delete, name='team_delete'),
)
