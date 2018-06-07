from __future__ import division

import numpy
import mathops
from optical_element import OpticalElement


class WavePlate(OpticalElement):

    def __init__(self, degrees_retardance=90):

        OpticalElement.__init__(self)

        # these need not be orthogonal
        self.fast_axis = [1, 0, 0]
        self.slow_axis = [0, 1, 0]

        # defaults based on calcite, and in general dependent upon wavelength
        self.ne = 1.486
        self.n0 = 1.658

        self.degrees_retardance = degrees_retardance

        # matrices
        phase = 1j*numpy.pi*self.degrees_retardance/360
        self.jones = numpy.array([[numpy.exp(phase), 0], [0, numpy.exp(-phase)]])  # fast axis along x-hat
        self.mueller = mathops.jones2mueller(self.jones)
