# DUKA
[![Build Status](https://travis-ci.org/kipkemei/duka.svg?branch=master)](https://travis-ci.org/kipkemei/duka)
 Click this link to view Travis Ci builds
the live version is at https://duka.herokuapp.com .

You can try logging in as superuser with admin@gmail.com password 1


## Create a database user and the application database:
createuser duka <br>
createdb my_db --owner duka_user <br>
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

<p><strong>/etc/supervisor/conf.d/duka.conf</strong></p>

<figure class="highlight"><pre><code class="language-text" data-lang="text">[program:duka-train]
command=/home/duka/bin/gunicorn_start
user=duka
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/duka/logs/gunicorn-error.log</code></pre></figure>

<p>Reread Supervisor configuration files and make the new program available:</p>
sudo supervisorctl reread <br />
sudo supervisorctl update

<p>Add a new configuration file named <strong>duka</strong> inside <strong>/etc/nginx/sites-available/</strong>:</p>

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">sudo vim /etc/nginx/sites-available/duka</code></pre></figure>

<p><strong>/etc/nginx/sites-available/duka</strong></p>

<figure class="highlight"><pre><code class="language-nginx" data-lang="nginx"><span class="k">upstream</span> <span class="s">app_server</span> <span class="p">{</span>
    <span class="kn">server</span> <span class="s">unix:/home/duka/run/gunicorn.sock</span> <span class="s">fail_timeout=0</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">server</span> <span class="p">{</span>
    <span class="kn">listen</span> <span class="mi">80</span><span class="p">;</span>

    <span class="c1"># add here the ip address of your server
</span>    <span class="c1"># or a domain pointing to that ip (like example.com or www.duka.herokuapp.com)
</span>    <span class="kn">server_name</span> <span class="mi">107</span><span class="s">.178.28.172</span><span class="p">;</span>
upstream app_server {
    server unix:/home/duka/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;

    # add here the ip address of your server
    # or a domain pointing to that ip (like example.com or www.example.com)
    server_name 107.170.28.172;

    keepalive_timeout 5;
    client_max_body_size 4G;

    access_log /home/duka/logs/nginx-access.log;
    error_log /home/duka/logs/nginx-error.log;

    location /static/ {
        alias /home/duka/static/;
    }

    # checks for static file, if not found proxy to app
    location / {
        try_files $uri @proxy_to_app;
    }

    location @proxy_to_app {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_pass http://app_server;
    }
}
    
</span></code></pre></figure>

<p>Create a symbolic link to the <strong>sites-enabled</strong> dir:</p>

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">sudo ln -s /etc/nginx/sites-available/duka /etc/nginx/sites-enabled/duka</code></pre></figure>

<hr>
<hr><br>
<span class="nb">source </span>bin/activate
<span class="nb">cd </span>duka
git pull origin master
python manage.py collectstatic
python manage.py migrate
sudo supervisorctl restart duka
<span class="nb">exit</span></code></pre></figure>

<hr /


# Docker

## there may be issues using docker because am using one of those old computers which doesn't have VT-X/AMD-v (Virtualization technology)   Keep calm though because i will be updating it soon. I have also made major configurations and i have availed necessary files. if you are a developer you cant be troubled making the changes or you may wait atleast a day and it gonna be alright

