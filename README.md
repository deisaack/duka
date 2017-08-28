# DUKA
[![Build Status](https://travis-ci.org/kipkemei/duka.svg?branch=master)](https://travis-ci.org/kipkemei/duka)

the live version is at https://duka.herokuapp.com .

You can try logging in as superuser with admin@gmail.com password 1


## Create a database user and the application database:
createuser u_urban <br>
createdb urban_prod --owner u_urban <br>
psql -c "ALTER USER u_urban WITH PASSWORD '123'" <br>

### clone the repo after creating a virtualenv. and add this to the /home/user/bin/gunicorn_start

#!/bin/bash

NAME="urban_train"
DIR=/home/urban/urban-train
USER=urban
GROUP=urban
WORKERS=3
BIND=unix:/home/urban/run/gunicorn.sock
DJANGO_SETTINGS_MODULE=urban_train.settings
DJANGO_WSGI_MODULE=urban_train.wsgi
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
