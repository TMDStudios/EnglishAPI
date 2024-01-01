from django.urls import path
from . import views

urlpatterns = [
    path('', views.getWords),
    path('level/<int:level>/<int:activity>', views.getWordsByLevel),
    path('add/', views.addWord),
    path('level/<int:level>/delete', views.deleteTable),
    path('leaderboard/', views.getLeaderboard),
    path('leaderboard/<int:level>', views.getLeaderboardLevel),
    path('leaderboard/add/', views.addTime),
    path('mistakes/', views.getMistakes),
    path('mistakes/add/', views.addMistake),
    path('bannerclicks/', views.getBannerClicks),
    path('bannerclicks/add/', views.addBannerClick),
    path('games/add/', views.addGame),
    path('games/', views.getGames),
    path('unapproved-games/', views.getUnapprovedGames)
]