from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.text)


class MainPage(models.Model):
    slider_text = models.CharField(max_length=250)
    slider_item = models.ManyToManyField(Skill)
    slider_content = models.TextField()
    slider_image = models.ImageField(upload_to="uploads/image", null=True, blank=True)
    slider_button_text = models.CharField(max_length=250)
    slider_button_file = models.FileField(upload_to="uploads/mycv", null=True, blank=True)

    def __str__(self):
        return str(self.id)
