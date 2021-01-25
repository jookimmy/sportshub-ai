from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render



def index(request):
    return render(request, "nba_tweets/index.html",{"content":"tweet"})

def get_tweets(request):
    '''
    if request.is_ajax:
        tweets = serializers.serialize('json', [, ]) 
        return JsonResponse({"tweets": tweets}, status = 200)
    '''
    return render(request, "nba_tweets/index.html",{"content":"hi"})