#! /usr/bin/python3

import asyncio
import urllib.request
import sys
import datetime

from obswsrc import OBSWS
from obswsrc.requests import StartStopStreamingRequest


def logger(logmessage):
    f = open("log.txt", "a")
    f.write(str(datetime.datetime.now()) + " " + logmessage + "\n")
    f.close


async def main():
 
    try:
        # set the IP of the OBS computer here
        obsws = OBSWS('10.11.0.124', 4444, "password")
        # if no response from OBS in 30 seconds EXIT
        await asyncio.wait_for(obsws.connect(), timeout=30)

        logger("Connection established.")

        while True:

            event = await obsws.event()

            logger(str(format(event.type_name)))

            if(format(event.type_name) == "StreamStarting"):
                # change the IP to the Screenly OSE computer
                # this is the asset_id of the RTMP streaming asset in Screely OSE
                HitURLToLoadAsset = urllib.request.urlopen("http://10.11.0.159/api/v1/assets/control/asset&b0983c0918b94856900040d9a9e8bdbf").read()
                logger(str(HitURLToLoadAsset))

            if(format(event.type_name) == "StreamStopped"):
                # change the IP to the Screenly OSE computer
                # this is another asset in Screely OSE
                HitURLToLoadAsset = urllib.request.urlopen("http://10.11.0.159/api/v1/assets/control/asset&3b2fb67002364b269d0c2674a628533c").read()
                logger(str(HitURLToLoadAsset))

    except asyncio.TimeoutError:
        logger("OBS NOT RUNNING-- TIMEOUT!")

    except OSError:
        logger("OBS IS NOT RUNNING")

    except:
        logger(str(sys.exc_info()[1]))

    finally:
        await obsws.close()
        logger("Connection terminated.")
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
