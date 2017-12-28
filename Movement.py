# PiMotor
import PiMotor

#System
from time import sleep
from signal import pause
from random import randrange

#bluetooth
from bluetooth import *

#Custom Imports
import  MoveConstants

#Setup Motors
rightMotor = PiMotor.Motor(MoveConstants.RIGHT_MOTOR, 1)
leftMotor = PiMotor.Motor(MoveConstants.LEFT_MOTOR, 1)

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

'''
Directional code is <Motor><F/R><Speed 0-100>
Example:
LF50 = Left Motor, Forward, Speed 50
LR25 = Left Motor, Reverse, Speed 25
RR25 = Right Motor, Reverse, Speed 25
RF100 = Right Motor, Forward, Speed 100
'''

try:
    while True:
        data = client_sock.recv(1024)
        if ( len(data) != 0 ):
            # some string received
            print "received [%s]" % data
            motor = data[0]
            direction = data[1]
            speed = data[2:]
            if ( speed < 0 or speed > 100 ):
                print "Defaulting speed to 100"
                speed = 100
            if ( motor == "R" ):
                if ( direction == "F" ):
                    rightMotor.forward(speed)
                elif ( direction == "R" ):
                    rightMotor.reverse(speed)
            if ( motor == "L" ):
                if ( direction == "F" ):
                    leftMotor.forward(speed)
                elif( direction == "R" ):
                    leftMotor.reverse(speed)
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"
