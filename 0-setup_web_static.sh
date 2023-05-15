#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
    echo "Installing Nginx..."
    sudo apt update
    sudo apt install -y nginx
    echo "Nginx installed successfully."
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

echo "Hello, world!" | sudo tee /data/web_static/releases/test/index.html > /dev/null



sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
sudo sed -i "/server_name _;/a \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" $config_file
sudo service nginx restart