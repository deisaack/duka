# DUKA
[![Build Status](https://travis-ci.org/kipkemei/duka.svg?branch=master)](https://travis-ci.org/kipkemei/duka)

the live version is at https://duka.herokuapp.com .

You can try logging in as superuser with admin@gmail.com password 1


## Create a database user and the application database:
createuser duka <br>
createdb my_db --owner u_urban <br>
psql -c "ALTER USER admin WITH PASSWORD '123'" <br>

### clone the repo after creating a virtualenv. and add this to the /home/user/bin/gunicorn_start

#!/bin/bash

NAME="duka"
DIR=/home/duka/duka
USER=duka
GROUP=duka
WORKERS=3
BIND=unix:/home/duka/run/gunicorn.sock
DJANGO_SETTINGS_MODULE=duka.settings
DJANGO_WSGI_MODULE=duka.wsgi
LOG_LEVEL=error

cd $DIR
source ../bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-


<hr />

