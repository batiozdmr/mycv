from apps.parameter.models import Menu, Settings


def site_settings(request):
    settings = Settings.objects.filter().last()
    return {'settings': settings}


def menu(request):
    menu_list = Menu.objects.filter().order_by("alignment")
    return {'menu_list': menu_list}
