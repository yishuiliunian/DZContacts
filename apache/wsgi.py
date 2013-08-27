import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'DZContacts.settings'
app_apth = "/home/dz/DZContacts/"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()
