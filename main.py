#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_color_sensor = ColorSensor(Port.S4) 
right_color_sensor = ColorSensor(Port.S3) 

calibration_mode = False
execute_program = True

RED = 10
GREEN = 10
BLUE = 20

turn_rate = 60
drive_speed = 120

ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=127)

if (calibration_mode):
    execute_program = False
    while True:
        red, green, blue = color_sensor.rgb()
        is_black = red < RED or blue < BLUE or green < GREEN
        print("Red: {}, Green: {}, Blue: {},".format(red, green, blue))
        print(str(is_black))
        wait(100)


while (execute_program):
    red, green, blue = color_sensor.rgb()
    is_black = red < RED or blue < BLUE or green < GREEN

    if is_black:
        robot.drive(drive_speed, -turn_rate)
    else:
        robot.drive(drive_speed, turn_rate)
