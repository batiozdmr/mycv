from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    profile_image = models.ImageField()
    birth_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user.username)



