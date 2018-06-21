
from __future__ import division

import matplotlib.pyplot as plt

import numpy
from polarizer import Polarizer
from waveplate import WavePlate
from incoherent import Incoherent
from compound_element import CompoundElement

if __name__ == '__main__':

    # create optical elements

    horizontal_polarizer = Polarizer()

    vertical_polarizer = Polarizer()
    vertical_polarizer.absolute_rotate(90)

    compensator = WavePlate(degrees_retardance=360 * (2*18 / 560))

    # make incoherent, linearly polarized light. Horizontal/along x-axis
    light = Incoherent()
    linearly_polarized_light = numpy.matmul(horizontal_polarizer.mueller, light.stokes_vector)

    # just normalizing relative to newly-polarized beam's intensity
    linearly_polarized_light /= linearly_polarized_light[0]

    angles = []
    intensities = []
    for degrees in numpy.linspace(0, 360, 500):
        compensator.absolute_rotate(degrees)
        M = numpy.matmul(compensator.mueller, horizontal_polarizer.mueller)
        M = numpy.matmul(vertical_polarizer.mueller, M)
        stokes = numpy.matmul(M, linearly_polarized_light)
        intensities.append(stokes[0, 0].real)
        angles.append(degrees)

    plt.plot(angles, intensities)
    plt.show()

