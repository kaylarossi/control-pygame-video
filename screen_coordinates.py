#
# kmr262 3/9/22 quit_button.py
#
import os
import time
import RPi.GPIO as GPIO
import pygame 
from pygame.locals import* #for event mouse variables

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.putenv('SDL_VIDEODRIVER', 'fbcon') #Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb0')  #
os.putenv('SDL_MOUSEDRV', 'TSLIB') #track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode((320,240))

my_font = pygame.font.Font(None, 25)
my_buttons = {'quit':(60,200)}
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
coordlist = []

while button_run:
    screen.fill(black)
    now = time.time()
    elaptime = now - starttime
# time quit
    if elaptime > timeout:  
        button_run = False

# look for touches/coordinates
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos

            if y>160:
                if x<100:
                    print ("quit pressed")
                    button_run = False
                    #print(coordlist)

            print("touch at " + str(pos))
            #append to list of touches
            coordlist.append(pos)

    #print out coorindates on center screen
    text2_surface = my_font.render("touch at " + str(pos) , True, white)
    rect2 = text2_surface.get_rect(center=(160, 120))
    screen.blit(text2_surface, rect2)

    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, white)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    pygame.display.flip()

#physical quit button
    if (not GPIO.input(27)):
        button_run = False

print(coordlist)
