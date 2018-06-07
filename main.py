
import numpy
import mathops
from waveplate import WavePlate
from polarizer import Polarizer

# TODO check jones matrices


if __name__ == '__main__':

    # make a circular polarizer
    linear_polarizer = Polarizer()
    wave_plate = WavePlate(degrees_retardance=90)

    # rotate wave-plate by 45 degrees
    m = mathops.rotate_mueller(wave_plate.mueller, 45)

    mueller_circular = numpy.matmul(m, linear_polarizer.mueller)

    dbg = 1