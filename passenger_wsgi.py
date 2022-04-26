# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1068039/data/www/rwp-ras.ru/rwprop')
sys.path.insert(1, '/var/www/u1068039/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rwprop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
