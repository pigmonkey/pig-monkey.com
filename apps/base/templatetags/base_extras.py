from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, url):
    try:
        pattern = reverse(url)
    except:
        pass
    else:
        if len(pattern) > 1:
            if request.path.startswith(pattern):
                return "active"
        else:
            if request.path == pattern:
                return "active"
    return ""
