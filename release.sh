#!/bin/bash

poetry run python -m manage migrate

fixtures=$(ls seeds/)

while IFS= read -r fixture; do
    echo -n "Seeding "
    echo $fixture
    poetry run python -m manage loaddata seeds/$fixture
done <<< "$fixtures"

poetry run python -m manage collectstatic --noinput
