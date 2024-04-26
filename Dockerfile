FROM python:3.10-bullseye
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry install -n
COPY . .
EXPOSE 8000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
