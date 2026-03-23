from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, Event


# Create your views here.

def index(request):
    context = {"user" : False, "admin" : False}
    print(request.session.keys())
    if "user" in request.session:
        print("user")
        context["user"] = request.session["user"]
        context["username"] = request.session["username"]
        context["balance"] = request.session["balance"]
        if request.session["admin"]:
            context["admin"] = True
    events = Event.objects.all()
    context["events"] = events
    return render(request, "tickets/index.html", context=context)

def login(request):
    return render(request ,"tickets/login.html")

def logout(request):
    del request.session["user"]
    del request.session["username"]
    del request.session["balance"]
    del request.session["admin"]
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
            request.session["admin"] = False
        if u.admin:
            request.session["admin"] = True
    return redirect("/")
