from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addWord),
    path('leaderboard/', views.getLeaderboard),
    path('leaderboard/add/', views.addTime)
]