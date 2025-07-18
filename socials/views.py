from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "socials/home.html")
