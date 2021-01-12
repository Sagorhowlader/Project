from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Like
from notifications.models import Notification


def user_liked_post(sender, instance, *args, **kwargs):
    like = instance
    print(like)
    post = like.post
    print(post)
    sender = like.user
    print(sender)
    notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
    notify.save()

post_save.connect(Like.user_liked_post, sender=Like)





