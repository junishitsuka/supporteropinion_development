from django.db import models
from mongoengine import Document, StringField, IntField, signals
import datetime

# Create your models here.
# class Base(Document):
#     meta = {
#         'abstract': True
#     }

class Tweet(Document):
    _id = IntField(required=True)
    screen_name = StringField(required=True)
    text = StringField(required=True)
    created_at = StringField(required=True)
    tweet_id = IntField(required=True)
    team_id = IntField(required=True)
    retweet_count = IntField(required=True)
    favorite_count = IntField(required=True)
