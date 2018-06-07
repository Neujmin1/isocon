from optical_element import OpticalElement
import numpy


class Polarizer(OpticalElement):

    def __init__(self):

        OpticalElement.__init__(self)

        self.jones = numpy.array([[1, 0], [0, 0]])  # transmission axis along x-hat

        m = 0.5*numpy.ones([4, 4])
        m[2:, :] = 0
        m[:, 2:] = 0
        self.mueller = m  # transmission axis along x-hat/horizontal

        # depolarization?

        # contrast ratio?

        #



