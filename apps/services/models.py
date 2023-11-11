from django.db import models


class ServicesSettings(models.Model):
    text = models.CharField(max_length=200)
    content = models.TextField()

    def service_list(self):
        services = Services.objects.filter().order_by("alignment")
        return services

    def __str__(self):
        return str(self.text)


class Services(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    content = models.TextField()
    alignment = models.IntegerField()

    def __str__(self):
        return str(self.text)
