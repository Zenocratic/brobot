#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Turn on (true) or off (false) calibration mode 
calibration_mode = False

# Enter measured reflection of RGB-light
RED_ON_WHITE = 100
RED_ON_BLACK = 0

GREEN_ON_WHITE = 100
GREEN_ON_BLACK = 0

BLUE_ON_WHITE = 100
BLUE_ON_BLACK = 0

# Calculate thresholds
RED = (RED_ON_WHITE + RED_ON_BLACK) // 2
GREEN = (GREEN_ON_WHITE + GREEN_ON_BLACK) // 2
BLUE = (BLUE_ON_WHITE + BLUE_ON_BLACK) // 2

# Initiate EV3 & BroBot
ev3 = EV3Brick()
robot = BroBot()
execute_program = True

# Calibration loop: prints measured values every 100ms
if (calibration_mode):
    execute_program = False
    i = 0
    while True:
        rgb = robot.measure_color()
        left_is_black = rgb[0] < RED and rgb[1] < GREEN and rgb[2] < BLUE
        right_is_black = rgb[3] < RED and rgb[4] < GREEN and rgb[5] < BLUE
        print("\nLEFT\tR: {0[0]}\tG: {0[1]}\tB: {0[2]}\tBLACK: {1}\nRIGHT\tR: {0[3]}\tG: {0[4]}\tB: {0[5]}\tBLACK: {2}\n".format(rgb, left_is_black, right_is_black))
        wait(100)


turn_rate = 60
drive_speed = 120

while (execute_program):
    red, green, blue = color_sensor.rgb()
    is_black = red < RED or blue < BLUE or green < GREEN

    if is_black:
        robot.drive(drive_speed, -turn_rate)
    else:
        robot.drive(drive_speed, turn_rate)
