from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Thread(models.Model):
    title = models.CharField()
    description = models.TextField()
    sticky = models.BooleanField(default=False)
    created_at = models.DateTimeField()


class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()
