from django.urls import path
from .views import * 
from classroom import views

urlpatterns = [
     path('',views.Home, name="Home"),
     path('dashboard',views.Dashboard, name="Dashboard"),
     path('graph', views.Graph, name="Graph"),
]
