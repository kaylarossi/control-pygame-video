#
# kmr262 3/9/22 two_button.py
#
import os
import subprocess
import time
import RPi.GPIO as GPIO
import pygame 
from pygame.locals import* #for event mouse variables
#import two_collide

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Display on piTFT environment settings
os.putenv('SDL_VIDEODRIVER', 'fbcon') 
os.putenv('SDL_FBDEV', '/dev/fb0') 
#track mouse clicks on piTFT
os.putenv('SDL_MOUSEDRV', 'TSLIB') 
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode((320,240))

my_font = pygame.font.Font(None, 25)
my_buttons = {'quit':(80,180), 'start':(240,180)}
screen.fill(black)  #erase workspace

for my_text, text_pos in my_buttons.items():
    text_surface = my_font.render(my_text, True, white)
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)
pygame.display.flip()

button_run = True
timeout = 30
starttime = time.time()
pos = pygame.mouse.get_pos()

while button_run:

    screen.fill(black)  #clear screen
    now = time.time()
    elaptime = now - starttime
#time bail out
    if elaptime > timeout:  
        button_run = False
#GPIO physical bail out
    if (not GPIO.input(27)):
        button_run = False
#Display start and quit buttons
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, white)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)
#Display screen coordinates
    #print("touch at " + str(pos))
    text2_surface = my_font.render("touch at " + str(pos), True, white)
    rect2 = text2_surface.get_rect(center=(160,120))
    screen.blit(text2_surface, rect2)

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos

            if y > 120:
                if x < 160:
                    print ("quit pressed")
                    button_run = False
                if x >= 160:
                    print("start pressed")
                    # play two_collide when start pressed
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
                        #print("collided")

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
                        #init for quit mouse press
                        for event in pygame.event.get():
                            if(event.type is MOUSEBUTTONDOWN):
                                pos=pygame.mouse.get_pos()
                            elif(event.type is MOUSEBUTTONUP):
                                pos = pygame.mouse.get_pos()
                                x,y = pos
                                if y>120:
                                    if x< 160:
                                        code_run = False
                                        #button_run = False

                        ballrect1 = ballrect1.move(speed1)
                        ballrect2 = ballrect2.move(speed2)

                        screen.fill(black)
                        screen.blit(ball1, ballrect1)
                        screen.blit(ball2, ballrect2)
                        
                    #physical quit
                        if (not GPIO.input(27)):
                            code_run = False

                    #display quit and start buttons
                        for my_text, text_pos in my_buttons.items():
                            text_surface = my_font.render(my_text, True, white)
                            rect = text_surface.get_rect(center=text_pos)
                            screen.blit(text_surface, rect)

                    #print and display screen coordinates
                        text2_surface = my_font.render("touch at " + str(pos), True, white)
                        rect2 = text2_surface.get_rect(center=(160,120))
                        screen.blit(text2_surface, rect2)

                        pygame.display.flip()

    pygame.display.flip()

