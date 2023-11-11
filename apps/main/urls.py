from django.urls import path

from apps.main.views import index

urlpatterns = [
    path('', index, name="main"),
]
