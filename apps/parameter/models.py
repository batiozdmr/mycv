from django.db import models


class Settings(models.Model):
    text = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="uploads/image", null=True, blank=True)

    def __str__(self):
        return str(self.text)


class Menu(models.Model):
    text = models.CharField(max_length=100)
    slug = models.CharField(max_length=250)
    alignment = models.IntegerField()

    def __str__(self):
        return str(self.text)
