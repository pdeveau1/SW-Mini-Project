from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TwitterAPIView,
    TwitterUserAPIView,
    IsBotAPIView,
    SentimentAPIView
)

urlpatterns = [
    path('user/',TwitterAPIView.as_view()),
    path('user/<str:username>',TwitterUserAPIView.as_view()),
    path('isbot/<str:username>',IsBotAPIView.as_view()),
    path('sentiment/<str:username>',SentimentAPIView.as_view())
]