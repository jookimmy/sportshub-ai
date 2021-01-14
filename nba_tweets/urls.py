from django.urls import path
from . import views

urlpatterns = [
    # path("admin/",),
    path('', views.index, name='index'),
    path('get/tweets', views.get_tweets, name = "get_tweets"),
]
