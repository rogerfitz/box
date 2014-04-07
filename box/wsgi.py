from django.core.wsgi import get_wsgi_application
from dj_static import Cling

settings.configure()
application = Cling(get_wsgi_application())
