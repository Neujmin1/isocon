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

    def general_mueller(self, rotation_degrees_ccw):
        # general formula of linear polarizer of given rotation

        rads = rotation_degrees_ccw*numpy.pi/180

        c2 = numpy.cos(2*rads)
        s2 = numpy.sin(2*rads)

        r1 = numpy.array([1, c2, s2, 0])
        r2 = numpy.array([c2, c2*c2, c2*s2, 0])
        r3 = numpy.array([s2, c2*s2, s2*s2, 0])
        r4 = numpy.array([0, 0, 0, 0])

        return 0.5*numpy.matrix(numpy.array([r1, r2, r3, r4]))

    def general_jones(self, rotation_degrees_ccw):

        rads = rotation_degrees_ccw * numpy.pi / 180

        c1 = numpy.cos(2*rads)
        s1 = numpy.sin(2*rads)

        r1 = numpy.array([c1*c1, c1*s1])
        r2 = numpy.array([c1*s1, s1*s1])

        return numpy.matrix(numpy.array([r1, r2]))






