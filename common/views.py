# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from common.models import Team, Tweets, Datecount, Words

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

def team_show(request, team_id=None):
    team = Team.objects(team_id=team_id)
    if not(team): raise Http404

    datecount = Datecount.find_datecount(team_id, '2015-04-17', '2015-04-25')
    datelist = [(d.date).encode('utf8') for d in datecount]
    countlist = [d.count for d in datecount]

    trendwords = Words.find_trendwords(team_id, '2015-04-17', '2015-04-25')

    return render_to_response(
        'teams/team_show.html',
        {'team': team[0], 'datelist': datelist, 'countlist': countlist, 'trendwords': trendwords},
        context_instance=RequestContext(request)
    )

def team_tweet(request, team_id=None):
    team = Team.objects(team_id=team_id)
    if not(team): raise Http404

    positive_tweet = Tweets.find_positive_tweet(team_id, 3)
    negative_tweet = Tweets.find_negative_tweet(team_id, 3)

    return render_to_response(
        'teams/team_tweet.html',
        {'team': team[0], 'positive_tweet': positive_tweet, 'negative_tweet': negative_tweet},
        context_instance=RequestContext(request)
    )
