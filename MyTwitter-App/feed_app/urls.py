from django.urls import path
from feed_app import views

urlpatterns = [
    path('', views.myfeed, name='myfeed'),
    path('like_tweet/<tweet_id>/', views.like_tweet, name='like_tweet'),
    path('dislike_tweet/<tweet_id>/', views.dislike_tweet, name='dislike_tweet'),
    path('delete/<tweet_id>/', views.delete_tweet, name='delete_tweet'),
]
