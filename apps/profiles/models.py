from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    profile_image = models.ImageField()
    birth_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user.username)


class Education(models.Model):
    text = models.CharField(max_length=200)
    content = models.TextField()
    year = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return str(self.text)


class Skill(models.Model):
    text = models.CharField(max_length=200)
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.text)


