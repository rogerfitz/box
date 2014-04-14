from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import newrelic.agent
import os

config_file = os.environ.get('NEW_RELIC_CONFIG_FILE')
environment = 'production'#os.environ.get('NEW_RELIC_ENVIRONMENT')

newrelic.agent.initialize(config_file, environment)

application = Cling(get_wsgi_application())
