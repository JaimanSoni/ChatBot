from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    owner = models.ForeignKey(User,  on_delete = models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
