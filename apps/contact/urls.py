from django.conf.urls import *
from views import contact

urlpatterns = patterns('',
    url(r'^$',
        view=contact,
        name="contact"
    ),
)
