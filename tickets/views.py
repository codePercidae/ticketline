from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.

def index(request):
    context = {"user" : False}
    print(request.session.keys())
    if "user" in request.session:
        print("user")
        context["user"] = request.session["user"]
        context["username"] = request.session["username"]
        context["balance"] = request.session["balance"]
    return render(request, "tickets/index.html", context=context)

def login(request):
    return render(request ,"tickets/login.html")

def logout(request):
    del request.session["user"]
    del request.session["username"]
    del request.session["balance"]
    return redirect("/")

def auth(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    result = User.objects.filter(username = username)
    for u in result:
        if u.password == password:
            request.session["user"] = u.id
            request.session["username"] = u.username
            request.session["balance"] = u.balance
    return redirect("/")
    