from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^gear/', include('geartracker.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/$',
        view = TemplateView.as_view(template_name='about.html'),
        name = 'about'
    ),
    url(r'^code/$',
        view = TemplateView.as_view(template_name='code.html'),
        name = 'code'
    ),
    url(r'^photos/$',
        view = TemplateView.as_view(template_name='photos.html'),
        name = 'photos'
    ),
    url(r'^key.asc$',
        view = RedirectView.as_view(url="%skey.asc" % settings.STATIC_URL),
        name = 'public_key'
    ),
    url(r'^what/$',
        view = RedirectView.as_view(url='/about/', permanent=True),
    ),
    url(r'^who/$',
        view = RedirectView.as_view(url='/about/', permanent=True),
    ),
    url('', include('vellum.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
