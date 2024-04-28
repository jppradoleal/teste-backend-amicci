#!/bin/bash

poetry run python -m manage migrate

mkdir log
touch /app/log/access.log

fixtures=$(ls seeds/)

while IFS= read -r fixture; do
    echo -n "Seeding "
    echo $fixture
    poetry run python -m manage loaddata seeds/$fixture
done <<< "$fixtures"

poetry run python -m \
    gunicorn amicci.asgi:application \
    -k uvicorn.workers.UvicornWorker -w 3 \
    -b 0.0.0.0:8000 --log-level=info \
    --access-logfile=/app/log/access.log -t 120
