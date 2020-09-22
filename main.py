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
BLUE = 20

turn_rate = 60
drive_speed = 120

ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=121)

def entertainment(number):
    if number == 1:
       robot.turn(45)
       robot.turn(-90)
       robot.turn(45)
    elif number == 2:
        ev3.speaker.say("Never gonna give you up.")
    elif number == 3:
        for i in range(1,10):
            ev3.light.on(Color.RED)
            wait(100)
            ev3.light.on(Color.GREEN)
            wait(100)
            ev3.light.on(Color.BLUE)
            wait(100)
        ev3.light.off
    else:
        ev3.speaker.play_file(SoundFile.DOG_BARK_1)

# TODO Increase turn radius while outside black line
# Write your program here.
ev3.speaker.beep()
start_time = time.time()

if (debug_mode):
    while True:
        execute_program = False
        red, green, blue = color_sensor.rgb()
        is_black = red < RED or blue < BLUE or green < GREEN
        print("Red: {}, Green: {}, Blue: {},".format(red, green, blue))
        print(str(is_black))


while (execute_program):
    red, green, blue = color_sensor.rgb()
    is_black = red < RED or blue < BLUE or green < GREEN

    if is_black:
        robot.drive(-drive_speed, -turn_rate)
    else:
        robot.drive(-drive_speed, turn_rate)

    if us_sensor.distance() < 100:
        robot.stop()
        break

    if time.time() - start_time >= 10:
        robot.stop()
        entertainment(random.randint(1,4))
        start_time = time.time()

ev3.speaker.play_file(SoundFile.CHEERING)