from picamera import PiCamera
from time import sleep, localtime, strftime
from fractions import Fraction
from datetime import datetime, time, tzinfo, timedelta 
import requests


t = localtime()
localHour = t[3]
count = 1

def normalCam():
    with PiCamera() as camera:
    #camera.start_preview()
	camera.resolution = (1920,1080)
        camera.vflip = True
	sleep(2)
        Photoname = strftime("%Y_%m_%d_%H_%M_%s")
        camera.capture('/home/pi/Pictures/{}.jpg'.format(Photoname))
        print('NormalFilter: Captured {}'.format(Photoname))
        sleep(10)# wait 5 minutes


def lowLightCam():
    with PiCamera() as camera:
	camera.vflip = True
        camera.resolution = (1920, 1080)
        # Set a framerate of 1/6fps, then set shutter
        # speed to 6s and ISO to 800
        camera.framerate = Fraction(1, 6)
        camera.shutter_speed = 6000000
        camera.exposure_mode = 'off'
        camera.iso = 800
        # Give the camera a good long time to measure AWB
        # (you may wish to use fixed AWB instead)
        sleep(10)
        # Finally, capture an image with a 6s exposure. Due
        # to mode switching on the still port, this will take
        # longer than 6 seconds
        Photoname = strftime("%Y-%m-%d--%H:%M:%s")
        camera.capture('/home/pi/Pictures/{}.jpg'.format(Photoname))
        print("LowLightFilter: Captured {}".format(count))

def hourCheck():
    dt = datetime.today()
    currentTime = dt.hour, dt.minute, dt.second
    print("{}:{}:{}".format(currentTime[0],currentTime[1], currentTime[2]))
    if currentTime < (5, 30, 1) or currentTime > (18, 50, 1):
        lowLightCam()
        pass
    else:
        normalCam()
        pass
        

# Begin photo programs here
while True:
    print(count)
    hourCheck()
    sleep(1)
    count = count + 1
    
