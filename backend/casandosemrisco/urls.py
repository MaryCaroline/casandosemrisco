from django.conf.urls import  include, url, static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView

import django_js_reverse.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^casandosemrisco/', include('core.urls')),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', RedirectView.as_view(url='casandosemrisco')),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
