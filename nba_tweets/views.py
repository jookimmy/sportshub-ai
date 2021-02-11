from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from rest_framework import serializers


# how to manually serialize without a model
class MySerializer(serializers.Serializer):
    TweetID = serializers.CharField()
    Text = serializers.CharField()
    URL = serializers.CharField()
    QuoteID = serializers.CharField()
    ReplyID = serializers.CharField()


# allows database to be stored as a dictionary for easier accesibility
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def index(request):
    # accesses data from the database and pushes to front end    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tweets;")
        x = dictfetchall(cursor)
    return render(request, "nba_tweets/index.html",{"tweets":x})

# allows database to be stored as a dictionary for easier accesibility
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_tweets(request):

    if request.is_ajax:
        tweets = MySerializer(x).data
        return JsonResponse({"tweets": tweets}, status = 200)
