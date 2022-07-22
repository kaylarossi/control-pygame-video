#
# kmr262 3/5/22 two_collide.py
#
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')  #play on piTFT

import pygame
pygame.init()
pygame.mouse.set_visible(False) #hides mouse cursor

width = 320
height = 240
speed1 = [30,30]
speed2 = [20,20]
black = (0,0,0)

screen = pygame.display.set_mode([width, height])
ball1 = pygame.image.load("/home/pi/lab2_files_s22/xmas_ball.png")
ball2 = pygame.image.load("/home/pi/lab2_files_s22/wire_ball.png")

ballrect1 = ball1.get_rect()
ballrect1.x = 100
ballrect1.y = 50
ballrect2 = ball2.get_rect()
ballrect2.x = 200
ballrect2.y = 100

code_run = True
while code_run:
    time.sleep(0.2)
    collide = ballrect1.colliderect(ballrect2)
    print("collided")

    if collide == True:
        speed1[0] = -speed1[0]
        speed1[1] = -speed1[1]
        speed2[0] = -speed2[0]
        speed2[1] = -speed2[1]

    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = - speed2[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    ballrect1 = ballrect1.move(speed1)
    ballrect2 = ballrect2.move(speed2)

    if (not GPIO.input(27)):  #quit button
        code_run = False

    screen.fill(black)
    screen.blit(ball1, ballrect1)
    screen.blit(ball2, ballrect2)
    pygame.display.flip()

