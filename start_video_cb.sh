#!/bin/bash
#
#kmr262 3/2/22 start_video_cb.sh
#
python3 more_video_control_cb.py &
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/video_fifo /home/pi/bigbuckbunny320p.mp4
