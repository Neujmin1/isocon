import matplotlib.pyplot as plt

from polarizer import Polarizer
from waveplate import WavePlate
from mirror import Mirror
from compound_element import CompoundElement
from incoherent import Incoherent
import numpy


if __name__ == '__main__':

    # create a few optical elements
    polarizer1 = Polarizer()  # this object will remain fixed

    waveplate1 = WavePlate(degrees_retardance=90)
    waveplate1.absolute_rotate(45)

    mirror1 = Mirror()
    #mirror1.absolute_rotate(45) # this may be necessary if you actually use the mueller matrix of the mirror

    # always present order for light wave coming from the right
    compound_item = CompoundElement([mirror1, waveplate1])  # this object will be rotated

    # make incoherent, linearly polarized light
    light = Incoherent()
    linearly_polarized_light = numpy.matmul(polarizer1.mueller, light.stokes_vector)  # along x-axis

    # just normalizing relative to newly-polarized beam's intensity
    linearly_polarized_light /= linearly_polarized_light[0]

    angles = []
    intensities = []
    for degrees in numpy.linspace(0, 90, 100):
        compound_item.absolute_rotate(degrees)
        stokes = numpy.matmul(compound_item.mueller, linearly_polarized_light)
        stokes = numpy.matmul(polarizer1.mueller, stokes)
        intensities.append(stokes[0, 0].real)
        angles.append(degrees)

    plt.plot(angles, intensities)
    plt.show()