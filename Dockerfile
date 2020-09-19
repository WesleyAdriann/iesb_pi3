FROM python:3.8-alpine3.10

WORKDIR /code

COPY ./code .

ENTRYPOINT python3 ./main.py