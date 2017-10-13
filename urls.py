from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from website.views.site import HomepePageView

admin.site.site_header = 'Rigips Trophy'


urlpatterns = [
    url('^$', HomepePageView.as_view(), name='website.index'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
