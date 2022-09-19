from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import TwitterUser
from .serializers import TwitterUserSerializer
import twitter.user as twitter
class TwitterUserAPIView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        '''
        Helper method to get the object with given twitter handle
        '''
        try:
            return TwitterUser.objects.get(username = username)
        except TwitterUser.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        twitter_instance = self.get_object(request.data.get('username'))
        if not twitter_instance:
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
        else:
            serializer = TwitterUserSerializer(twitter_instance)
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class IsBotAPIView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, username):
        '''
        Helper method to get the object with given twitter handle
        '''
        try:
            return TwitterUser.objects.get(username = username)
        except TwitterUser.DoesNotExist:
            return None

    def get(self, request, username, *args, **kwargs):
        twitter_instance = self.get_object(username)
        if not twitter_instance:
            return Response(
                {"res": "Object with twitter id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TwitterUserSerializer(twitter_instance)
        return Response(serializer.data['is_bot'], status=status.HTTP_200_OK)
    