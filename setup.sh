#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Not run as root. Rerun with sudo"
  exit
fi

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Internet connected. Let's do an update..."
    sudo apt-get update -y
    sudo apt-get full-upgrade -y
else
    echo "No internet connection. Won't do update..."
fi

echo "creating basic storage location"
mkdir -p /home/pi/.p_stor/
touch /home/pi/.p_stor/data.json
sudo mkdir -p /lib/systemd/system/
sudo touch /lib/systemd/system/roommonitor.service
sudo echo " 
[Unit]
 Description=Room Monitor
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python /home/pi/server.py

 [Install]
 WantedBy=multi-user.target" >> /lib/systemd/system/roommonitor.service
 
sudo chmod 644 /lib/systemd/system/roommonitor.service
 
sudo systemctl daemon-reload
sudo systemctl enable roommonitor.service

echo "Done. Restarting to apply changes"
sudo reboot
