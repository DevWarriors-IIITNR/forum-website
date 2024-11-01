from datetime import datetime
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import logout
from .models import Post, Comment, PostForm, CommentForm
from allauth.socialaccount.models import SocialAccount


def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        args = {"posts": posts}
        return render(request, "test.html", args)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def newpost(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                # post.created_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                post.save()
                return redirect("/")
        else:
            form = PostForm()
        return render(request, "newpost.html", {"form": form})
    else:
        return redirect(pleasesignin)


def pleasesignin(request):
    return render(request, "pleasesignin.html")


def logout_view(request):
    logout(request)
    return redirect("/")
