from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation.trans_real import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.URLField()
    is_banned = models.BooleanField(default=False)


@receiver(user_signed_up)
def create_user_profile(sender, request, user, **kwargs):
    data = SocialAccount.objects.filter(user=user).values()
    Profile.objects.create(
        user=user,
        picture=data[0]["extra_data"]["picture"],
        is_banned=False,
    )


@receiver(user_signed_up)
def save_user_profile(sender, request, user, **kwargs):
    user.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) + " by " + str(self.user) + " on " + str(self.created_at)


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

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
