from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Tweets


def index(request):
    return render(request, "nba_tweets/index.html",{"content":"tweet"})

def get_tweets(request):

    if request.is_ajax:
        tweets = serializers.serialize('json', [Tweets.objects.all(), ]) 
        return JsonResponse({"tweets": tweets}, status = 200)
