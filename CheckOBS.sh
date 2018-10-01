#!/bin/bash

if pgrep -x "nginx"
then
    echo $(date -u) "NGINX Running" >> /home/pi/scripts/OBS.log
else
    echo $(date -u) "NGINX Stopped" >> /home/pi/scripts/OBS.log
    sudo /usr/local/nginx/sbin/nginx
    echo $(date -u) "NGINX Started" >> /home/pi/scripts/OBS.log
fi


if [ -e /home/pi/scripts/OBS.lock ]
then
  echo $(date -u) "OBS python script already running... exiting!" >> /home/pi/scripts/OBS.log
  exit
fi

touch /home/pi/scripts/OBS.lock

        echo $(date -u) "START OBS Script" >> /home/pi/scripts/OBS.log
        /home/pi/scripts/OBS.py
        echo $(date -u) "STOP OBS Script" >> /home/pi/scripts/OBS.log

rm /home/pi/scripts/OBS.lock
