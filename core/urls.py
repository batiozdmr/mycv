from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('', include("apps.main.urls"), name="index"),
    path('contact/', include("apps.contact.urls"), name="contact"),
    path('admin/', admin.site.urls),
    path('rosetta/lang/trans/', include('rosetta.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
