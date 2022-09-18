from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Twitter_User(models.Model):
    username = models.CharField(max_length = 15) #usernames can only be 15 characters on twitter
    is_bot = models.BooleanField(default=False)
    topics = JSONField(max_length=200)
    sentiment = models.CharField(max_length = 15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    #Tells Django what to print when it needs to print out an instance of the Twitter_User model
    def __str__(self):
        return self.username