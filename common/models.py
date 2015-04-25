from django.db import models
from mongoengine import Document, StringField, IntField, signals
from dateutil.parser import parse
from dateutil.relativedelta import *
from datetime import timedelta

# Create your models here.
# class Base(Document):
#     meta = {
#         'abstract': True
#     }

class Tweets(Document):
    _id = StringField(required=True)
    screen_name = StringField(required=True)
    text = StringField(required=True)
    created_at = StringField(required=True)
    tweet_id = IntField(required=True)
    team_id = IntField(required=True)
    retweet_count = IntField(required=True)
    favorite_count = IntField(required=True)

    @classmethod
    def count_team_tweet(self, team_id):
        return self.objects.filter(team_id=team_id).count()

    @classmethod
    def oldest_tweet_time(self, team_id):
        tweet = self.objects.filter(team_id=team_id).order_by('+tweet_id').limit(1)
        time_ja = parse(tweet[0].created_at) + timedelta(hours=9)
        return time_ja.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def newest_tweet_time(self, team_id):
        tweet = self.objects.filter(team_id=team_id).order_by('-tweet_id').limit(1)
        time_ja = parse(tweet[0].created_at) + timedelta(hours=9)
        return time_ja.strftime('%Y-%m-%d %H:%M:%S')
 
class Team(Document):
    _id = StringField(required=True)
    team_id = IntField(required=True)
    name = StringField(required=True)
