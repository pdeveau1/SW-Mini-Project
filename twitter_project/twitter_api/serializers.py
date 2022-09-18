from rest_framework import serializers
from .models import TwitterUser
class TwitterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterUser
        fields = ["username", "is_bot", "sentiment", "topics", "user"]