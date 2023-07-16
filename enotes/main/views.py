from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/login")
def pmanager(request):
    w = models.passwords.objects.all()
    content = {
        "passwords": w,
        "author": request.user
    }
    return render(request, 'pmanager.html', content)

@login_required(login_url="/login")
def notes(request):
    return render(request, 'notes.html')

@login_required(login_url="/login")
def noteview(request):
    q = models.note.objects.all()
    content = {
        "note": q,
        "author": request.user,
    }
    return render(request, "noteview.html", content)

def submit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["notepad"]
        user = request.user
    models.note.objects.create(author=user,title=title, content=content )
    return redirect("/notes")

def log(request):
    return render(request, "login.html")

def auth(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
    user = authenticate(request, username=name, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        return redirect("/login")

def signup(request):
    return render(request, "signup.html")

def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]
    User.objects.create_user(username=name, email=email, password=password)
    return redirect("/login")

def logou(request):
    logout(request)
    return redirect("/login")

def addpass(request):
    if request.method == "POST":
        site = request.POST["site"]
        password = request.POST["password"]
    models.passwords.objects.create(author=request.user, site=site, passtr=password)
    return redirect("/pmanager")

def notecheck(request, id):
    q = models.note.objects.get(id=id)
    m = {"note": q}
    return render(request, "notecheck.html", m)
