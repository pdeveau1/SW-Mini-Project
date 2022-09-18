from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    username = models.CharField(max_length = 15)
    is_bot = models.BooleanField(default = False, blank = True)
    sentiment = models.CharField(max_length = 180)
    topics = models.CharField(max_length = 180)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.username