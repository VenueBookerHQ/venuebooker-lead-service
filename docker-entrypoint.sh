#!/bin/bash
python manage.py migrate                  
python manage.py collectstatic --noinput  
python manage.py loaddata web_app/fixtures/initial_data.json

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn base_site.wsgi:application \
    --name venuebooker-api-service \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"
