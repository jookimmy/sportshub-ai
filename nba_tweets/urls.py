from django.urls import path
from . import views

urlpatterns = [
    # path("admin/",),
    path('', views.index, name='index'),
]
