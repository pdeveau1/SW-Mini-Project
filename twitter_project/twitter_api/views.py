from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import TwitterUser
from .serializers import TwitterUserSerializer
import twitter.user as twitter
class TwitterUserAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        bot = twitter.User(request.data.get('username'))
        data = {
            'username': request.data.get('username'),
            'is_bot': bot.get_bot(),
            'sentiment': bot.calc_sentiment(),
            'topics': "hello"
        }
        serializer = TwitterUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    