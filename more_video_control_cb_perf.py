#
# kmr262 3/2/22 more_video_control_cb_perf.py
#
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM) #set broadcom numbering
#set up piTFT buttons with pull up
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#callback routine setup

def GPIO17_callback(channel):
    print("falling edge detected on 17")
    cmd17 = 'echo "pause" > /home/pi/video_fifo'
    subprocess.check_output(cmd17, shell=True)

def GPIO22_callback(channel):
    print("falling edge detected on 22")
    cmd22 = 'echo "seek 10 0" > /home/pi/video_fifo'
    subprocess.check_output(cmd22, shell=True)

def GPIO23_callback(channel):
    print("falling edge detected on 23")
    cmd23 = 'echo "seek -10 0" > /home/pi/video_fifo'
    subprocess.check_output(cmd23, shell=True)

def GPIO27_callback(channel):
    global code_run
    print("falling edge detected on 27")
    cmd27 = 'echo "quit" > /home/pi/video_fifo'
    subprocess.check_output(cmd27, shell=True)
    code_run=False

def GPIO13_callback(channel):
    print("falling edge detected on 13")
    cmd13 = 'echo "seek 30 0" > /home/pi/video_fifo'
    subprocess.check_output(cmd13, shell=True)

def GPIO26_callback(channel):
    print("falling edge detected on 26")
    cmd26 = 'echo "seek -30 0" > /home/pi/video_fifo'
    subprocess.check_output(cmd26, shell=True)

#connect callback routine to GPIO

GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=GPIO13_callback, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)

code_run = True

time.sleep(10)

    
#clean up GPIO on normal exit
GPIO.cleanup() 
