from django.urls import path
from . import views

urlpatterns = [
    path('', views.getWords),
    path('level/<int:level>', views.getWordsByLevel),
    path('add/', views.addWord),
    path('leaderboard/', views.getLeaderboard),
    path('leaderboard/<int:level>', views.getLeaderboardLevel),
    path('leaderboard/add/', views.addTime)
]