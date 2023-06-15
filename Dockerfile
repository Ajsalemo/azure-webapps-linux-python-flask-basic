FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

<<<<<<< HEAD
ENTRYPOINT [ "/app/init_container.sh" ]
=======
CMD ["gunicorn", "-b", "0.0.0.0", "app:app", "--timeout 600"]
>>>>>>> 16d4a8dd562c7191e7222b24007dc6578c95f88f

EXPOSE 8000