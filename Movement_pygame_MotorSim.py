# PiMotor
import PiMotor

#GPIO
#from gpiozero import LED
#from gpiozero import PWMLED
#from gpiozero import DigitalOutputDevice

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
#backward = DigitalOutputDevice(MoveConstants.GPIO_BACKWARD_PIN)
#frontward = DigitalOutputDevice(MoveConstants.GPIO_FORWARD_PIN)
leftMotor = PiMotor.Motor( "MOTOR1", 1 )
rightMotor = PiMotor.Motor( "MOTOR2", 1 )

#Setup to detect keyboard -- this should be taken out with bluetooth
pygame.init()
screen = pygame.display.set_mode((200,200))

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print ("UP Key")
                    #frontward.blink(on_time=0.5,n=1)
                    leftMotor.forward( 50 )
                    rightMotor.forward( 50 )
                elif event.key == pygame.K_DOWN:
                    print ("DOWN Key")
                    leftMotor.reverse( 50 )
                    rightMotor.reverse( 50 )
                elif event.key == pygame.K_LEFT:
                    leftMotor.reverse( 50 )
                    rightMotor.forward( 50 )
                elif event.key == pygame.K_RIGHT:
                    leftMotor.forward( 50 )
                    rightMotor.reverse( 50 )
                elif event.key == pygame.K_ESCAPE:
                    leftMotor.stop()
                    rightMotor.stop()

except KeyboardInterrupt:
    print("\Exiting MotorSim\n")
