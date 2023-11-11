from django.shortcuts import render

from apps.main.models import MainPage


def index(request):
    main_page = MainPage.objects.filter().last()
    context = {
        'main_page': main_page
    }
    return render(request, "index.html", context)
