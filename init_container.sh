#!/bin/bash

gunicorn -b 0.0.0.0 app:app --timeout 600 & \
    gunicorn app:app -w 3 --certfile /app/cert.pem --keyfile /app/key.pem -b 0.0.0.0:8443