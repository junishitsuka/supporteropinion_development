# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from common.models import Team, Tweets

# Create your views here.
def team_list(request):
    teams = list(Team.objects.all().order_by('id'))
    for i,v in enumerate(teams):
        teams[i].tweet_count = Tweets.count_team_tweet(v['team_id'])
        teams[i].oldest = Tweets.oldest_tweet_time(v['team_id'])
        teams[i].newest = Tweets.newest_tweet_time(v['team_id'])
    return render_to_response(
        'teams/team_list.html',
        {'teams': teams},
        context_instance=RequestContext(request)
    )

def team_edit(request, team_id=None):
    return HttpResponse(u'書籍の編集')

def team_delete(request, team_id=None):
    return HttpResponse(u'書籍の編集')

def team_show(request, team_id=None):
    print team_id
    return render_to_response(
        'teams/team_show.html',
        {'teams': teams},
        context_instance=RequestContext(request)
    )
