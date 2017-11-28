#GPIO
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import DigitalOutputDevice

#System
from time import sleep
from signal import pause
from random import randrange

#pygame
import pygame

#bluetooth
from bluetooth import *

#Custom Imports
import  MoveConstants

#Setup pins
backward = DigitalOutputDevice(MoveConstants.GPIO_BACKWARD_PIN)
frontward = DigitalOutputDevice(MoveConstants.GPIO_FORWARD_PIN)

#Setup to detect keyboard -- this should be taken out with bluetooth
pygame.init()
screen = pygame.display.set_mode((200,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print ("UP Key")
                frontward.blink(on_time=0.5,n=1)
            elif event.key == pygame.K_DOWN:
                print ("DOWN Key")
                backward.blink(on_time=0.5,n=1)

