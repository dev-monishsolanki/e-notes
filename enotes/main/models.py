from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now

# Create your models here.

class note(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="not set")
    content = models.TextField()
    published = models.DateTimeField(default=now, editable=False)
    due = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username

class passwords(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.TextField(default=" ")
    passtr = models.CharField(max_length=20, default="Not set")

    def __str__(self):
        return self.author.username
