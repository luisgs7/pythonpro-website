release: python manage.py sync_roles
web: newrelic-admin run-program gunicorn pythonpro.wsgi --log-file -
worker: newrelic-admin run-program celery --app pythonpro.celery worker --loglevel=info
