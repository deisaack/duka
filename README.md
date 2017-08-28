# DUKA
[![Build Status](https://travis-ci.org/kipkemei/duka.svg?branch=master)](https://travis-ci.org/kipkemei/duka)

the live version is at https://duka.herokuapp.com .

You can try logging in as superuser with admin@gmail.com password 1


## Create a database user and the application database:
createuser u_urban
createdb urban_prod --owner u_urban
psql -c "ALTER USER u_urban WITH PASSWORD '123'"

