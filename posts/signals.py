from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Like
from notifications.models import Notification


@receiver(post_save, sender=Like.user)
def user_like_post(sender, instance, created, **kwargs):
    print("fuck")





