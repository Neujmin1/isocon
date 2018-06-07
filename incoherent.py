from light import Light
import numpy


class Incoherent(Light):

    def __init__(self):

        Light.__init__(self)

        self.stokes_vector = numpy.array([1, 0, 0, 0])  # (I, M, C, S) un-polarized state
        self.stokes_vector.shape = (4, 1)  # ensure it's a column vector
