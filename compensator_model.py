
from __future__ import division

from mirror import Mirror
from polarizer import Polarizer
from waveplate import WavePlate
from incoherent import Incoherent

if __name__ == '__main__':

    # create optical elements

    horizontal_polarizer = Polarizer()

    vertical_polarizer = Polarizer()
    vertical_polarizer.absolute_rotate(90)

    tca_18 = WavePlate(degrees_retardance=360*(18/560))
    tca_35 = WavePlate(degrees_retardance=360*(35/360))

