#!/bin/bash

# Get env vars in the Dockerfile to show up in the SSH session
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)

gunicorn -b 0.0.0.0:8000 app:app --timeout 600 --access-logfile '-' --error-logfile '-'