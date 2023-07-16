from django.contrib import admin
from django.urls import path
from main import views

admin.site.site_header = "NoteHub Admin"
admin.site.site_title = " NoteHub Admin Portal"
admin.site.index_title = "Welcome to NoteHub Portal"

urlpatterns = [
  path("",views.index, name='main'),
  path("pmanager", views.pmanager, name='password'),
  path("addnotes",views.notes, name='notes'),
  path("submit", views.submit, name="submit"),
  path("login", views.log, name="login"),
  path("signup", views.signup, name="signup"),
  path("auth", views.auth, name="auth"),
  path("create", views.create, name="create"),
  path("logout", views.logou, name="logout"),
  path("notes", views.noteview, name="view"),
  path("addpass", views.addpass, name="addpass"),
  path("notes/<str:id>", views.notecheck, name="check"),
]
