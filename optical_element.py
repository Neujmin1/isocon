import mathops
import numpy


class OpticalElement:

    def __init__(self):

        # in general, these 3 could be a lookup table via empirical lambda-dependence
        self.transmission = 1
        self.reflection = 0
        self.absorbtion = 0
        self.degrees_rotated_ccw = 0  # measured ccw from x-axis. Light along z-axis
        self.attitude = numpy.eye(3)  # orientation in 3D (reserved for advanced operations)

        # dispersion relation?

        # AR coating?

        self.jones = None
        self.mueller = None

    def relative_rotate(self, degrees_ccw=45):

        self.mueller = mathops.rotate_mueller(self.mueller, degrees_ccw)
        self.jones = mathops.rotate_jones(self.jones, degrees_ccw)
        self.degrees_rotated_ccw += degrees_ccw

    def absolute_rotate(self, degrees_ccw=0):

        relative_degrees_to_rotate = degrees_ccw - self.degrees_rotated_ccw
        self.relative_rotate(relative_degrees_to_rotate)
        self.degrees_rotated_ccw = degrees_ccw
