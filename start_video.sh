#!/bin/bash
#
# kmr262 3/6/22 start_video.sh
#
# bash script to launch mplayer and 'more_video_control.py'
#
python3 more_video_control.py & 
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/video_fifo /home/pi/bigbuckbunny320p.mp4 
