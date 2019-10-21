from django.db import models
from django.contrib.auth.models import User

from api.constants import KNOWLEDGE_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True, unique=True)
    username = models.CharField(max_length=30, blank=True, unique=True)
    age = models.IntegerField(null=True, blank=True)
    is_guest = models.BooleanField(default=True)
    is_host = models.BooleanField(default=False)
    knowledge = models.IntegerField(choices=KNOWLEDGE_CHOICES)
    def __str__(self):
        return self.user.username

class Question(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Stand(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    # image = models.ImageField(upload_to = 'stand_images/', default = 'stand_images/None/no-img.jpg')
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class StandDescription(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    knowledge = models.IntegerField(choices=KNOWLEDGE_CHOICES)
    def __str__(self):
        return self.stand.name + self.knowledge
