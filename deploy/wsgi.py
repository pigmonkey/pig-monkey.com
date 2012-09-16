import os
import site
import sys

# Tell wsgi to add the Python site-packages to it's path.
site.addsitedir('/home/pigmonkey/.virtualenvs/pigmonkey/lib/python2.7/site-packages')

# Calculate the path based on the location of the WSGI script.
project = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pm')
sys.path.append(project)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pm.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Add the apps directory to the path.
import settings
sys.path.append(settings.PROJECT_ROOT)
