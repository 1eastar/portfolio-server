FROM        python:3.8.1-slim
MAINTAINER  ehdwls6703@gmail.com

RUN         apt -y update && apt -y dist-upgrade
RUN         apt -y install build-essential
RUN         apt -y install nginx supervisor
RUN         apt -y install libpcre3 libpcre3-dev python-dev

# WORKDIR     /srv
# RUN         python -m venv myvenv
# RUN         . myvenv/bin/activate
# RUN         export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.8"
# RUN         export PYTHONPATH="${PYTHONPATH}:/srv/djangobackend/myvenv/lib/python3.8/site-packages"

ENV         PROJECT_DIR              /srv/pf_server

COPY        .                       ${PROJECT_DIR}
WORKDIR     /srv/pf_server
RUN         pip install -r requirements.txt
RUN         python manage.py makemigrations
RUN         python manage.py migrate
RUN         echo "from django.contrib.auth.models import User; User.objects.filter(username='1eastar').delete(); User.objects.create_superuser('1eastar', 'ehdwls6703@gmail.com', 'h9u0m4a2n!')" | python manage.py shell
WORKDIR     ${PROJECT_DIR}

RUN         cp -f ${PROJECT_DIR}/.config/nginx.conf           /etc/nginx
RUN         cp -f ${PROJECT_DIR}/.config/pf_server      /etc/nginx/sites-available

RUN         rm -f /etc/nginx/sites-enabled/*
RUN         ln -fs /etc/nginx/sites-available/pf_server                  /etc/nginx/sites-enabled

RUN         cp -f ${PROJECT_DIR}/.config/supervisor_app.conf  /etc/supervisor/conf.d

EXPOSE      80, 443

CMD         supervisord -n