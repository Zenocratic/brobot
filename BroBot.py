class BroBot():
    def __init__(self):
        left_motor = Motor(Port.B)
        right_motor = Motor(Port.C)
        self.brobot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=127)
        self.left_color_sensor = ColorSensor(Port.S4)
        self.right_color_sensor = ColorSensor(Port.S3)

    def measure_color(self):
        left = self.left_color_sensor()
        right = self.left_color_sensor()
        return left + right

    def is_black(self, color_sensor):
        pass

