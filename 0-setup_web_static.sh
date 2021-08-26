#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

if [ ! -x "$(command -v nginx)" ]
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

sudo echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

add="\\\n\
        location /hbnb_static/ {\\
            alias /data/web_static/current/;\\
            autoindex off;\\
        }"

sudo sed -i "/server_name _;/a $add" /etc/nginx/sites-available/default

sudo service nginx restart
