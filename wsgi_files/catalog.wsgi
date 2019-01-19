# flask-dance 
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# add your python files to the python path; this is needed to find the application.py file (where your flask app is located)
import sys
sys.path.insert(0, '/var/www/ItemCatalogApp')

# tell the application where the root is - required for loading templates.
from application import app as application
application.secret_key = b' bKWsWgI9U_viJc05F8-ja0pE'
application.root_path = '/var/www/ItemCatalogApp'
