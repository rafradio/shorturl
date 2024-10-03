from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello world!</h2>")

def shorts(request, name):
    interal = "https://www.w3schools.com/django/django_create_app.php"
    return redirect(interal)