from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from profiles.models import Profile



# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name="noti_post", blank=True, null=True)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


