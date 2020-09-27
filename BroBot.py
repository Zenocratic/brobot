class BroBot():
    def __init__(self):
        left_motor = Motor(Port.B)
        right_motor = Motor(Port.C)
        self.brobot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=127)
        self.left_color_sensor = ColorSensor(Port.S4)
        self.right_color_sensor = ColorSensor(Port.S3)

    def measure_color(self):
        return self.left_color_sensor() + self.right_color_sensor()

    def is_black(self, thresholds):
        rgb = self.measure_color()
        return rgb[0] < thresholds[0] and rgb[1] < thresholds[1] and rgb[2] < thresholds[2] and rgb[3] < thresholds[0] and rgb[4] < thresholds[1] and rgb[5] < thresholds[2]