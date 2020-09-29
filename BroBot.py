from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

class BroBot():
    def __init__(self):
        left_motor = Motor(Port.B)
        right_motor = Motor(Port.C)
        self.brobot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=127)
        self.left_color_sensor = ColorSensor(Port.S4)
        self.right_color_sensor = ColorSensor(Port.S2)

        self.ev3 = EV3Brick()

        self.RED_ON_WHITE = 57
        self.RED_ON_BLACK = 5

        self.GREEN_ON_WHITE = 55
        self.GREEN_ON_BLACK = 4

        self.BLUE_ON_WHITE = 100
        self.BLUE_ON_BLACK = 10

        self.RED = (self.RED_ON_WHITE + self.RED_ON_BLACK) // 2
        self.GREEN = (self.GREEN_ON_WHITE + self.GREEN_ON_BLACK) // 2
        self.BLUE = (self.BLUE_ON_WHITE + self.BLUE_ON_BLACK) // 2

    def calibrate(self):
        self.ev3.screen.print("Calibrating...\nL-SENSOR: WHITE\nR-SENSOR: BLACK\nPUSH A BUTTON\nTO CONTINUE")
        while True:
            if self.ev3.buttons.pressed():
                break
            continue
        rgb = self.left_color_sensor.rgb() + self.right_color_sensor.rgb()

        self.RED_ON_WHITE = rgb[0]
        self.GREEN_ON_WHITE = rgb[1]
        self.BLUE_ON_WHITE = rgb[2]

        self.RED_ON_BLACK = rgb[3]
        self.GREEN_ON_BLACK = rgb[4]
        self.BLUE_ON_BLACK = rgb[5]

        self.RED = (self.RED_ON_WHITE + self.RED_ON_BLACK) // 2
        self.GREEN = (self.GREEN_ON_WHITE + self.GREEN_ON_BLACK) // 2
        self.BLUE = (self.BLUE_ON_WHITE + self.BLUE_ON_BLACK) // 2

    def drive(self):
        execute_program = True
        no_line = False
        turn_rate = 5
        drive_speed = 30

        while True:
            while (no_line):
                turn_rate = 80
                drive_speed = 50
                right_red, right_green, right_blue = right_sensor.rgb()
                left_red, left_green, left_blue = left_sensor.rgb()
                right_is_black = right_red < RED or right_green < GREEN or right_blue < BLUE
                left_is_black = left_red < RED or left_green < GREEN or left_blue < BLUE
                if not right_is_black and not left_is_black:
                    brobot.drive(drive_speed, turn_rate)
                if left_is_black or right_is_black:
                    wait(100)
                    execute_program = True
                    no_line = False



            while (execute_program):
                turn_rate = 120
                drive_speed = 200 
                right_red, right_green, right_blue = right_sensor.rgb()
                left_red, left_green, left_blue = left_sensor.rgb()
                right_is_black = right_red < RED or right_green < GREEN or right_blue < BLUE
                left_is_black = left_red < RED or left_green < GREEN or left_blue < BLUE

            if not right_is_black and not left_is_black:
                brobot.drive(drive_speed, 0)
            elif right_is_black and left_is_black:
                brobot.drive(drive_speed, 0)
            elif left_is_black:
                brobot.drive(50, -turn_rate)
                start_time = time.time()
            elif right_is_black:
                brobot.drive(50, turn_rate)
                start_time = time.time()


            if time.time() - start_time >= 3:
                start_time = time.time()
                execute_program = False
                no_line = True

