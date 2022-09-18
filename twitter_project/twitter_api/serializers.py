from rest_framework import serializers
from .models import Twitter_User

class TwitterUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Twitter_User
        fields = ('username', 'is_bot', 'topics', 'sentiment', 'user')