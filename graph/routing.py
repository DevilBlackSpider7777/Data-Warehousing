from django.urls import path
from .consumers import Graphconsumer

ws_urlpatterns =[
    path('ws/graph/',Graphconsumer)
]