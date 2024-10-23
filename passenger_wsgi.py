import os
import sys

# Add your Django project's root directory to the Python path
sys.path.append('/home/davrotxk/kip_pax')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Major_project.settings')

# Import the Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()