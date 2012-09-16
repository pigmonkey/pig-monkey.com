from django.conf.urls.defaults import *
from views import contact

urlpatterns = patterns('',
    url(r'^$',
        view=contact,
        name="contact"
    ),
)
