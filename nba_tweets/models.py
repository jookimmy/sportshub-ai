from django.db import models

class Tweet(models.Model):
    tweet_id = models.IntegerField()
    screen_name = models.CharField(max_length=100)
    text = models.CharField(max_length=280)
    quote_tweet = models.IntegerField(null=True)
    url = models.CharField(max_length=100)


#status.user.screen_name, status.id, text, quote_tweet, url