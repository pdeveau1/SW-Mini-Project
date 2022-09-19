from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TwitterUserAPIView,
    IsBotAPIView
)

urlpatterns = [
    path('user/',TwitterUserAPIView.as_view()),
    path('isbot/<str:username>',IsBotAPIView.as_view())
]