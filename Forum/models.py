from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.title) + " by " + str(self.user) + " on " + str(self.created_at)


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return (
            str(self.post)
            + " by "
            + str(self.body)[:10]
            + "-"
            + str(self.user)
            + " on "
            + str(self.created_at)
        )


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
