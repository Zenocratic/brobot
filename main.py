#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time, random



# Create your objects here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S4) 
us_sensor = UltrasonicSensor(Port.S3)

execute_program = True

debug_mode = False

RED = 10
GREEN = 10
BLUE = 10

turn_rate = 10
drive_speed = -100

ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=127)

def entertainment(number):
    if number == 1:
        robot.turn(360)
    elif number == 2:
        ev3.speaker.say("Never gonna give you up.")
    elif number == 3:
        robot.turn(360)
    else:
        robot.turn(360)
    wait(250)

# TODO Increase turn radius while outside black line
# Write your program here.
ev3.speaker.beep()
start_time = time.time()

if (debug_mode):
    execute_program = False
    red, green, blue = color_sensor.rgb()
    print("Red: {}, Green: {}, Blue: {},".format(red, green, blue))
    print(str(is_black))


while (execute_program):
    red, green, blue = color_sensor.rgb()
    is_black = red < RED or blue < BLUE or green < GREEN

    if is_black:
        robot.drive(drive_speed, turn_rate)
    else:
        robot.drive(drive_speed, -turn_rate)

    if us_sensor.distance() < 200:
        robot.stop()
        break

    if time.time() - start_time >= 10:
        start_time = time.time()
        robot.stop()
        entertainment(random.randint(1,4))

ev3.speaker.play_file(SoundFile.CHEERING)