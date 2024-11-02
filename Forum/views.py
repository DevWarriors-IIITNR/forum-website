from datetime import datetime
from django.http.response import HttpResponseNotFound
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Post, Comment, PostForm, CommentForm
from allauth.socialaccount.models import SocialAccount


def home(request):
    if request.user.is_authenticated and not (request.user.profile.is_banned):
        posts = Post.objects.filter(is_deleted=False).order_by("-created_at")
        args = {"posts": posts}
        return render(request, "test.html", args)
    elif request.user.is_authenticated and request.user.profile.is_banned:
        return redirect(banned_view)
    return render(request, "index.html")


@login_required
@require_http_methods(["DELETE"])
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if post.user == request.user or request.user.is_staff:
        post.is_deleted = True
        post.save()
        posts = Post.objects.filter(is_deleted=False).order_by("-created_at")
        return render(request, "partials/postlist.html", {"posts": posts})


def about(request):
    return render(request, "about.html")


@login_required
def newpost(request):
    if not (request.user.profile.is_banned):
        form = PostForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                # post.created_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                post.save()
                return redirect("/viewpost/" + str(post.pk))
        else:
            form = PostForm()
        return render(request, "newpost.html", {"form": form})
    else:
        return redirect(banned_view)


def pleasesignin(request):
    if not (request.user.is_authenticated):
        return render(request, "pleasesignin.html")
    elif request.user.is_authenticated and request.user.profile.is_banned:
        return redirect(banned_view)
    else:
        return HttpResponseNotFound()


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def viewpost(request, pk):
    if not request.user.profile.is_banned:
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post, is_deleted=False).order_by(
            "-created_at"
        )
        if request.method == "POST":
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = Post.objects.get(pk=pk)
                comment.save()
                return render(
                    request,
                    "partials/commentlist.html",
                    {"comments": comments, "post": post},
                )
        else:
            form = CommentForm()
        return render(
            request,
            "viewpost.html",
            {"form": form, "comments": comments, "post": Post.objects.get(pk=pk)},
        )
    else:
        return redirect(banned_view)


@login_required
@require_http_methods(["DELETE"])
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.user == request.user or request.user.is_staff:
        comment.is_deleted = True
        comment.save()
        comments = Comment.objects.filter(is_deleted=False, post=comment.post).order_by(
            "-created_at"
        )
        print(comments)
        return render(
            request,
            "partials/commentlist.html",
            {"comments": comments},
        )


@login_required
def banned_view(request):
    if request.user.profile.is_banned:
        return render(request, "youarebanned.html")
    else:
        return redirect("/")
