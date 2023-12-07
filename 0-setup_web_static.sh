#!/usr/bin/env bash
# Script sets up webservers for deployment of web_static
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
    sudo ufw allow 'Nginx HTTP'
    sudo service nginx start
fi

# Directories and subdirectories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link and deletes one if already there
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change owner
sudo chown -R ubuntu:ubuntu /data/

sudo tee /etc/nginx/sites-available/default > /dev/null << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current;
    }
}
EOF

# Restart nginx
sudo service nginx restart
