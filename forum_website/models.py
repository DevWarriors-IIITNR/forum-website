from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
