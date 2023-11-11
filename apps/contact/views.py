from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.contact.models import Contact


# Create your views here.

def contact(request):
    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and email and phone and message:
            control = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            if control:
                messages.success(request, "İşlem Başarılı")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                messages.warning(request, "Kayıt Başarısız")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.warning(request, "Lütfen Tüm alanları doldurun")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        messages.warning(request, "Geçerli bir istek gönderilemedi")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
