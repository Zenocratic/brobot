from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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

        print("RGB thresholds before: " + str(self.RED) + str(self.GREEN) + str(self.BLUE))

        self.RED = (self.RED_ON_WHITE + self.RED_ON_BLACK) // 2
        self.GREEN = (self.GREEN_ON_WHITE + self.GREEN_ON_BLACK) // 2
        self.BLUE = (self.BLUE_ON_WHITE + self.BLUE_ON_BLACK) // 2

        print("RGB thresholds after: " + str(self.RED) + str(self.GREEN) + str(self.BLUE))
