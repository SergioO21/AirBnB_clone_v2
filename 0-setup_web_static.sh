#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default

sudo service nginx restart
