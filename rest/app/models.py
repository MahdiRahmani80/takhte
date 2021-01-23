from django.db import models
from django.shortcuts import render, get_object_or_404
from django.conf import settings

class Post (models.Model):

    Text = models.TextField("Main Text")
    UserName = models.CharField("User Name", max_length = 100)
    Time = models.CharField("Time" , max_length = 100)
    Like = models.IntegerField()

    def __str__(self):
        return self.UserName

