
class OpticalElement:

    def __init__(self):

        # in general, these 3 could be a lookup table via empical lambda-dependence
        self.transmission = 1
        self.reflection = 0
        self.absorbtion = 0

        self.rotation_degrees = 0  # measured ccw from x-axis. Light along z-axis

        # dispersion relation?

        # how to handle AR coating?
