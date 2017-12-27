#GPIO
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import DigitalOutputDevice
from gpiozero import PWMOutputDevice

#System
from time import sleep
from signal import pause
from random import randrange

#bluetooth
from bluetooth import *

#Custom Imports
import  MoveConstants

#Setup pins
backward = DigitalOutputDevice(MoveConstants.GPIO_BACKWARD_PIN)
frontward = DigitalOutputDevice(MoveConstants.GPIO_FORWARD_PIN)
motor = PWMOutputDevice(MoveConstants.GPIO_MOTOR_PIN)

#Setup BT server
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
                   
print "Waiting for connection on RFCOMM channel %d" % port

client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

try:
    while True:
        data = client_sock.recv(1024)
        if ( data == "UP" ):
            print ("UP Key")
            frontward.blink(on_time=0.5,n=1)
        elif ( data == "DOWN" ):
            print ("DOWN Key")
            backward.blink(on_time=0.5,n=1)
        elif ( data == "MOTOR" ):
            motor.on()
            print (motor.value)
            motor.off()
        elif len(data) == 0: break
        print "received [%s]" % data
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"
