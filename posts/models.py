
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save


from profiles.models import Profile


# Create your models here.

class Post(models.Model):

    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
                              blank=True)
    video = models.FileField(upload_to='video_posts',
                             null=True, blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.content[:20]}--post by--{self.author}"

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body}-Comment by-{self.user}"

    # def user_comment_post(sender, instance, *args, **kwargs):
    #     commnet = instance
    #     post = commnet.post
    #     sender = commnet.user
    #     notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
    #     notify.save()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.Post
        sender = like.user
        notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
        notify.save()

# post_save.connect(Like.user_liked_post, sender=Like)
# # post_save.connect(Comment.user_comment_post, sender=Comment)