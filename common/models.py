# coding: utf8

from django.db import models
from mongoengine import Document, StringField, IntField, signals, FloatField, ListField
from dateutil.parser import parse
from dateutil.relativedelta import *
from datetime import timedelta, datetime

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
    pn_rate = FloatField()
    so_rate = FloatField()
    so_rate = FloatField()
    o_count = FloatField()
    p_count = FloatField()
    s_count = FloatField()
    n_count = FloatField()

    @classmethod
    def count_team_tweet(self, team_id):
        return self.objects(team_id=team_id).count()

    @classmethod
    def oldest_tweet_time(self, team_id):
        tweet = self.objects(team_id=team_id).order_by('+tweet_id').limit(1)
        time_ja = parse(tweet[0].created_at) + timedelta(hours=9)
        return time_ja.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def newest_tweet_time(self, team_id):
        tweet = self.objects(team_id=team_id).order_by('-tweet_id').limit(1)
        time_ja = parse(tweet[0].created_at) + timedelta(hours=9)
        return time_ja.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def find_positive_tweet(self, team_id, limit):
        return self.objects(team_id=team_id).order_by('-p_count').limit(limit)

    @classmethod
    def find_negative_tweet(self, team_id, limit):
        return self.objects(team_id=team_id).order_by('-n_count').limit(limit)

    @classmethod
    def aggregate_positive_tweet(self, team_id, start_date, end_date):
        positive_tweet = self._get_collection().aggregate([{"$match": {"team_id": team_id, "created_at": {"$gte": start_date, "$lte": end_date}}}, {"$group": {"_id": {"$substr": ["$created_at", 0, 10]}, "count": {"$sum": "$p_count"}}}])
        return positive_tweet

    @classmethod
    def aggregate_negative_tweet(self, team_id, start_date, end_date):
        # summary = {}
        # print type(start_date)
        # start_date = datetime.strptime(start_date, '%Y-%m-%d')
        # end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=+1)
        #
        # while start_date != end_date:
        #     next_date = start_date + timedelta(days=+1)
        #     summary[start_date.strftime('%Y-%m-%d')] = self._get_collection().aggregate([{"$match": {"team_id": team_id, "created_at": {"$gte": start_date.strftime('%Y-%m-%d'), "$lt": next_date.strftime('%Y-%m-%d')}}}, {"$group": {"_id": "created_at", "count": {"$sum": "$n_count"}}}])
        #     print summary[start_date.strftime('%Y-%m-%d')]
        #     start_date = next_date
        # return summary
        return self._get_collection().aggregate([{"$match": {"team_id": team_id, "created_at": {"$gte": start_date, "$lte": end_date}}}, {"$group": {"_id": {"$substr": ["$created_at", 0, 10]}, "count": {"$sum": "$n_count"}}}])

class Team(Document):
    _id = StringField(required=True)
    team_id = IntField(required=True)
    name = StringField(required=True)

class Datecount(Document):
    _id = StringField(required=True)
    date = StringField(required=True)
    count = IntField(required=True)
    team_id = IntField(required=True)

    @classmethod
    def find_datecount(self, team_id, start_date, end_date):
        return self.objects(team_id=team_id, date__gte=start_date, date__lte=end_date).order_by('+date')

class Words(Document):
    _id = StringField(required=True)
    date = StringField(required=True)
    team_id = IntField(required=True)
    words = ListField(required=True)

    @classmethod
    def find_trendwords(self, team_id, start_date, end_date):
        words = self.objects(team_id=team_id, date__gte=start_date, date__lte=end_date).order_by('-date')
        return [{'date': w.date, 'words': ', '.join(w.words)} for w in words]

class Pcounts(Document):
    _id = StringField(required=True)
    date = StringField(required=True)
    count = IntField(required=True)
    team_id = IntField(required=True)

    @classmethod
    def find_pcount(self, team_id, start_date, end_date):
        return self.objects(team_id=team_id, date__gte=start_date, date__lte=end_date).order_by('+date')

class Ncounts(Document):
    _id = StringField(required=True)
    date = StringField(required=True)
    count = IntField(required=True)
    team_id = IntField(required=True)

    @classmethod
    def find_ncount(self, team_id, start_date, end_date):
        return self.objects(team_id=team_id, date__gte=start_date, date__lte=end_date).order_by('+date')
