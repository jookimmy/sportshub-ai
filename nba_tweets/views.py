from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from . import streamlistener
from .models import Tweet

stream_listener = streamlistener.StreamListener

def index(request):
    return render(request, "nba_tweets/index.html",{"content":tweet})

def get_tweets(request):
    if request.is_ajax:
        new_tweet = Tweet(
            tweet_id = stream_listener.tweet_id,
            screen_name = stream_listener.screen_name,
            text = stream_listener.text,
            quote_tweet = stream_listener.quote_tweet,
            url = stream_listener.url,
        )
        tweets = serializers.serialize('json', [ new_tweet, ]) 
        return JsonResponse({"tweets": tweets}, status = 200)