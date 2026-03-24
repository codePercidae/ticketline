from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, Event

# Create your views here.

def index(request):
    context = {"user" : False, "admin" : False}
    print(request.session.items())
    if "user" in request.session:
        context["user"] = request.session["user"]
        context["username"] = request.session["username"]
        context["balance"] = request.session["balance"]
        context["shoppingcart"] = len(request.session["shoppingcart"])
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
    del request.session["shoppingcart"]
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
            request.session["shoppingcart"] = []
        if u.admin:
            request.session["admin"] = True
    return redirect("/")

def buy(request, event_id):
    event = Event.objects.filter(id = event_id)[0]
    context = {"event": event}
    return render(request, "tickets/buy.html", context)

def add_to_cart(request, event_id):
    request.session["shoppingcart"].insert(event_id)
    return redirect("/")