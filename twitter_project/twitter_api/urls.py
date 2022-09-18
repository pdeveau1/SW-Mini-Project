from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TwitterUserAPIView,
)

urlpatterns = [
    path('user/',TwitterUserAPIView.as_view())
]