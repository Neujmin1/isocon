
import numpy
import mathops
from waveplate import WavePlate
from polarizer import Polarizer
from incoherent import Incoherent

# TODO check jones matrices


if __name__ == '__main__':

    '''
    
    
    # make a circular polarizer
    linear_polarizer = Polarizer()  # along x-axis
    wave_plate = WavePlate(degrees_retardance=90)

    # rotate wave-plate by 45 degrees
    m = mathops.rotate_mueller(wave_plate.mueller, 45)

    mueller_circular = numpy.matmul(m, linear_polarizer.mueller)

    # now try rotating polarization to vertical
    hwp = WavePlate(degrees_retardance=180)
    m = mathops.rotate_mueller(hwp.mueller, 45)

    mueller_vertical = numpy.matmul(m, linear_polarizer.mueller)

    '''

    wp = WavePlate(degrees_retardance=90)  # 180 = half wave, 90 = quarter wave, etc

    h = wp.mueller
    h45 = mathops.rotate_mueller(h, 45)

    dbg = 1