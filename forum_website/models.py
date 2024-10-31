from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    picture = models.URLField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET("[deleted]"))
    created_at = models.DateTimeField()


class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField()
    body = models.TextField()
    thread = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET("[deleted]"))
    created_at = models.DateTimeField()
