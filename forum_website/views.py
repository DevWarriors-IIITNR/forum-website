from django.shortcuts import redirect, render
from django.contrib.auth import logout


def home(request):
    if request.user.is_authenticated:
        return render(request, "test.html")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def newpost(request):
    if request.user.is_authenticated:
        return render(request, "newpost.html")
    return redirect(pleasesignin)


def pleasesignin(request):
    return render(request, "pleasesignin.html")


def logout_view(request):
    logout(request)
    return redirect("/")
