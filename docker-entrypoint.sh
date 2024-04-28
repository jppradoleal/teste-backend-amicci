#!/bin/bash

bash ./release.sh

mkdir log
touch /app/log/access.log

poetry run python -m \
    gunicorn amicci.asgi:application \
    -k uvicorn.workers.UvicornWorker -w 3 \
    -b 0.0.0.0:8000 --log-level=info \
    --access-logfile=/app/log/access.log -t 120
