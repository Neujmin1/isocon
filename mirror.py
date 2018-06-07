from optical_element import OpticalElement
import numpy


class Mirror(OpticalElement):  # just changes phase by pi

    def __init__(self):
        OpticalElement.__init__(self)

        self.mueller = numpy.eye(4)
        self.mueller[2:, 2:] *= -1

        self.jones = numpy.array([[1, 0], [0, -1]])