FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8001

ENTRYPOINT [ "/app/init_container.sh" ]

