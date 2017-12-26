# RasPiMovement

This project describes steps to develop a Python application for your Raspberry Pi to control movement over bluetooth using an Android phone. The Python GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/) is used to control LED to simulate front and backward motion.

In later parts of this application, the LED simulation is changed to use an actual SB Components H bridge connector to control motors.

## Items Needed
1. Raspberry Pi 3
2. Breadboard
3. Connector Pin

## Steps
1. Circuit to light up LED to ensure power is connected
2. Enhance circuit to connect LED to GPIO pins
3. Develop Python script to turn LED on/off
4. Enhance Python script to turn LED on/off using keyboard inputs
5. Install pybluez and setup serial bluetooth adapter
6. Install Serial Bluetooth Terminal on your phone
7. Connect and control LED
8. Motor control

## Setup Bluetooth on RasPi

## Use of SB Components Motor API
https://github.com/sbcshop/motor-shield
