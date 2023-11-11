from django.shortcuts import render

from apps.main.models import MainPage
from apps.services.models import *


def index(request):
    main_page = MainPage.objects.filter().last()

    service_settings = ServicesSettings.objects.filter().last()

    context = {
        'main_page': main_page,
        'service_settings': service_settings,
    }
    return render(request, "index.html", context)
