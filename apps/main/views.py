from django.shortcuts import render

from apps.main.models import MainPage
from apps.profiles.models import Education, Skill
from apps.services.models import *


def index(request):
    main_page = MainPage.objects.filter().last()

    service_settings = ServicesSettings.objects.filter().last()
    education_list = Education.objects.filter().order_by("order")
    skill_list = Skill.objects.filter()
    context = {
        'main_page': main_page,
        'service_settings': service_settings,
        'education_list': education_list,
        'skill_list': skill_list,
    }
    return render(request, "index.html", context)
