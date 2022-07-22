#
# kmr262 3/6/22 more_video_control_perf.py
#
# control myplayer through a FIFO using python program and GPIO buttons
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

code_run = True
#inital time
inittime = time.time()

while code_run:
    time.sleep(0.2)
#determine when its been 10 seconds exit loop
    curtime = time.time()

    if (not GPIO.input(17)):
        otpt17 = 'echo "pause" > /home/pi/video_fifo'
        subprocess.check_output(otpt17, shell=True)

    if (not GPIO.input(22)):
        otpt22 = 'echo "seek 10 0" > /home/pi/video_fifo'
        subprocess.check_output(otpt22, shell=True)

    if (not GPIO.input(23)):
        otpt23 = 'echo "seek -10 0" > /home/pi/video_fifo'
        subprocess.check_output(otpt23, shell=True)

    if (not GPIO.input(27)):
        otpt27 = 'echo "quit" > /home/pi/video_fifo'
        subprocess.check_output(otpt27, shell=True)
        code_run = False

    if (not GPIO.input(13)):
        otpt13= 'echo "seek 30 0" > /home/pi/video_fifo'
        subprocess.check_output(otpt13, shell=True)

    if (not GPIO.input(26)):
        otpt26 = 'echo "seek -30 0" > /home/pi/video_fifo'
        subprocess.check_output(otpt26, shell=True)

    if  curtime - inittime > 10:
        code_run = False
