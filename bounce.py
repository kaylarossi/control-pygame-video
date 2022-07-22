#
# kmr262 3/5/22 bounce.py
#
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')

import pygame

pygame.init()
pygame.mouse.set_visible(False) #hides mouse cursor

width = 320
height = 240    
speed = [25,25]
black = (0,0,0)


screen = pygame.display.set_mode([width, height]) 
ball = pygame.image.load("/home/pi/lab2_files_s22/xmas_ball.png")
ballrect = ball.get_rect()

code_run = True
while code_run:
    time.sleep(0.2)
    # moves ball away from sides of screen
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)

    if (not GPIO.input(27)):
        code_run = False

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
