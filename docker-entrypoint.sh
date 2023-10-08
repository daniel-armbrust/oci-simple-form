#!/bin/sh
exec gunicorn --access-logfile - --error-logfile - -b 0.0.0.0:5000 app:app