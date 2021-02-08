from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db import connection



def index(request):
    return render(request, "nba_tweets/index.html",{"content":"tweet"})

# allows database to be stored as a dictionary for easier accesibility
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
  

def get_tweets(request):
    # accesses data from the database and pushes to front end    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tweets;")
        x = dictfetchall(cursor)

    if request.is_ajax:
        tweets = serializers.serialize('json', [Tweets.objects.all(), ]) 
        return JsonResponse({"tweets": tweets}, status = 200)
