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


try:
    while True:
        data = client_sock.recv(1024)
        if ( len(data) != 0 ):
            direction = data[0]
            if ( direction == "F" ):
               leftMotor.forward( MoveConstants.MOTOR_SPEED )
               rightMotor.forward( MoveConstants.MOTOR_SPEED )
            elif ( direction == "B" ):
                leftMotor.reverse( MoveConstants.MOTOR_SPEED )
                rightMotor.reverse( MoveConstants.MOTOR_SPEED )
            elif ( direction == "L" ):
                leftMotor.reverse( MoveConstants.MOTOR_SPEED )
                rightMotor.forward( MoveConstants.MOTOR_SPEED )
            elif ( direction == "R" ):
                leftMotor.forward( MoveConstants.MOTOR_SPEED )
                rightMotor.reverse( MoveConstants.MOTOR_SPEED )
            elif ( direction == "S" ):
                leftMotor.stop()
                rightMotor.stop()
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"
