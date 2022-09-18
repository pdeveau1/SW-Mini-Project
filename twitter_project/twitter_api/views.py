from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import TwitterUserSerializer
from .models import Twitter_User

class TwitterUserViewSet(viewsets.ModelViewSet):
    queryset = Twitter_User.objects.all().order_by('username')
    serializer_class = TwitterUserSerializer