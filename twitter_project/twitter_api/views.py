from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import TwitterUser
from .serializers import TwitterUserSerializer
import twitter.user as twitter

class TwitterAPIView(APIView):
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
                'topics': bot.calc_topics()
            }
            serializer = TwitterUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TwitterUserSerializer(twitter_instance)
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        twitter_instance = self.get_object(request.data.get('username'))
        if not twitter_instance:
            return Response(
                {"res": "Object with that twitter username does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        bot = twitter.User(request.data.get('username'))
        data = {
            'username': request.data.get('username'),
            'is_bot': bot.get_bot(),
            'sentiment': bot.calc_sentiment(),
            'topics': bot.calc_topics()
        }
        serializer = TwitterUserSerializer(instance = twitter_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def get(self, request, username, *args, **kwargs):
        twitter_instance = self.get_object(username)
        if not twitter_instance:
            return Response(
                {"res": "Object with Twitter username does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TwitterUserSerializer(twitter_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                {"res": "Object with Twitter username does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TwitterUserSerializer(twitter_instance)
        return Response(serializer.data['is_bot'], status=status.HTTP_200_OK)

class SentimentAPIView(APIView):
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
                {"res": "Object with Twitter username does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TwitterUserSerializer(twitter_instance)
        return Response(serializer.data['sentiment'], status=status.HTTP_200_OK)

class TopicsAPIView(APIView):
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
                {"res": "Object with Twitter username does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TwitterUserSerializer(twitter_instance)
        return Response(serializer.data['topics'], status=status.HTTP_200_OK)
    