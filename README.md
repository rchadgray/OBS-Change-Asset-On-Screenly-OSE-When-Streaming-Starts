# Monitor OBS using websockets so when streaming is started in OBS load RTMP Stream on Screenly OSE off of NGINX server

Install OBS then install the OBS Websocket plugin for OBS.  As of this writing i am using 4.4.0.

https://github.com/Palakis/obs-websocket/releases

Then install Screely OSE on a Raspberry Pi.  As of this writing i am using Sprint 7.

https://www.screenly.io/ose/

https://github.com/Screenly/screenly-ose/releases

Install NGINX on a computer.  I installed it on a Raspberry Pi via these instructions.  Please see the repository for my nginx.conf setup.

https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/

Start the NGINX software

sudo /usr/local/nginx/sbin/nginx

So now you have your OBS software installed and are ready to send a streaming signal to the NGINX computer.
Enter this url in OBS under Stream > Custom Streaming Server

http://ip_of_nginx_computer/live

Then start streaming.

To view the stream off of the NGINX server you can use VLC Media player and enter this into the "Open Network Stream".

rtmp://ip_of_nginx_computer/live

Now we need to add an RTMP asset to Screenly OSE that points to this URL.

rtmp://ip_of_nginx_computer/live

Now using the Screenly OSE API you can get the list of assets on the Screenly OSE with this URL.

http://ip_of_OSE_compuiter/api/v1.1/assets

Record the asset_id of the RTMP asset.

You can not use this asset_id with the API to load the asset like this.

http://ip_of_OSE_compuiter/api/v1/assets/control/asset&asset_id

You will need this URL in the Phython code to load the RTMP stream asset when the the buttons to Start Streaming is pressed in OBS.

Now onto the Python side of things.  I setup the Python scripting on the NGINX Raspberry Pi.  You need Python 3.5+ in order to use obs-ws-rc.  Be aware that Raspberry Pi's already have Python on them, but it is not version 3.5+.  You will need to make sure when you run the Python code you are using 3.5+ that you installed.  

https://github.com/KirillMysnik/obs-ws-rc

You need to install the following libraries in Python.

pip install obs-ws-rc

pip install websockets

pip install asyncio

To see if you already have these libraries you can run this via Python.  help("modules")

Next is to put the CheckOBS.sh and OBS_Monitor.py file in a new folder called scripts:

/home/pi/scripts/

You need to change the permissions of these files so they are executable

chmod +x /home/pi/scripts/CheckOBS.sh

chmod +x /home/pi/scripts/OBS_Monitor.py

Now is time to setup crontab jobs to execute the shell script CheckOBS.sh.  See the file crontab.txt for an example that i created.

No you need to change the addresses of the OBS computer and OSE computer in the files OBS_Monitor.py

These scripts also write log files so you can see what they are doing.

You can monitor the log files with

tail -f /home/pi/scripts/log.txt /home/pi/scripts/OBS.log