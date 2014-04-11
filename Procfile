#NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program command options
#web: gunicorn box.wsgi:application
web: newrelic-admin run-program python manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
