import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/ubuntu/email_auth/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/email_auth')
sys.path.append('/home/ubuntu/email_auth/ea')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ea.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/ubuntu/email_auth/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
