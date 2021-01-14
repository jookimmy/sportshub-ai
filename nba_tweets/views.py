from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from . import streamlistener

def index(request):
    return render(request, "nba_tweets/index.html")

def get_tweets(request):
    if request.is_ajax:
        tweets = serializers.serialize('json', [ streamlistener.StreamListener.tweet_list, ]) 
        return JsonResponse({"tweets": tweets}, status = 200)