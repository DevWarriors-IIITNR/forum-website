from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def test(request):
    return render(request, "test.html")


def newpost(request):
    return render(request, "newpost.html")
